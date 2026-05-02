#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys
import os
import io
import json
import zipfile
from pathlib import Path
from typing import Any, Dict, List

from flask import Flask, make_response, request
from flask_cors import CORS

current_dir = Path(__file__).parent
project_root = current_dir.parent.parent
sys.path.insert(0, str(project_root))

from src.parser.antlr_parser import AntlrBSLParser
from src.database.db_manager import DatabaseConnection
from src.rules.loader import RuleLoader
from src.rules.rule_registry import RuleRegistry
from src.visitor.rules.rule_checking_visitor import RuleCheckingVisitor
from src.visitor.collectors import VariableCollector, FunctionCollector
from src.visitor.factory import VisitorFactory

app = Flask(__name__)
CORS(app)

# Папка для временных файлов
TEMP_EXTRACT_DIR = os.path.join(project_root, "temp_extract")
os.makedirs(TEMP_EXTRACT_DIR, exist_ok=True)

REPORTS_DIR = os.path.join(project_root, "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

try:
    parser = AntlrBSLParser()
    print("Парсер инициализирован")
except Exception as e:
    print(f"Ошибка парсера: {e}")
    parser = None

DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'bsl_analyzer',
    'user': 'alina',
    'password': 'pizdecqwerty1234'
}

db = DatabaseConnection(**DB_CONFIG)
db_connected = db.connect()

rules = []
if db_connected:
    rule_loader = RuleLoader(db)
    rules = rule_loader.load_all_rules()
    RuleRegistry.register_many(rules)
    print(f"Загружено {len(rules)} правил из базы данных")
else:
    print("База данных недоступна")

def json_unicode(data, status=200):
    response = make_response(json.dumps(data, ensure_ascii=False, indent=2), status)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

@app.route("/", methods=["GET"])
def index():
    return json_unicode({
        "message": "1C Code Analyzer API",
        "endpoints": {
            "GET /api/health": "Проверка состояния сервера",
            "POST /api/analyze": "Анализ ZIP-архива с .bsl файлами"
        }
    }, 200)

@app.route("/api/health", methods=["GET"])
def health_check():
    return json_unicode({
        "status": "ok",
        "parser_ready": parser is not None,
        "db_connected": db_connected,
        "rules_loaded": len(rules)
    }, 200)

def collect_statistics(ast):
    var_collector = VariableCollector()
    func_collector = FunctionCollector()
    composite = VisitorFactory.create_composite_visitor([var_collector, func_collector])
    ast.accept(composite)
    return {
        "variables": {"total": len(var_collector.variables)},
        "functions": {"total": len(func_collector.functions)},
        "procedures": {"total": len(func_collector.procedures) if hasattr(func_collector, 'procedures') else 0}
    }

def extract_bsl_files_from_zip(zip_data: bytes, extract_dir: str) -> List[str]:
    """Распаковывает ZIP‑архив и возвращает список путей к .bsl‑файлам."""
    bsl_files = []
    os.makedirs(extract_dir, exist_ok=True)
    
    # Преобразуем bytes в файловый объект
    with zipfile.ZipFile(io.BytesIO(zip_data), 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                if file.endswith('.bsl'):
                    bsl_files.append(os.path.join(root, file))
    
    return bsl_files
    

def analyze_bsl_file(file_path: str) -> Dict[str, Any]:
    """Анализирует один .bsl‑файл и возвращает результаты."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        print(f"  Анализ файла: {os.path.basename(file_path)}")
        
        ast = parser.parse_string(code, os.path.basename(file_path))
        
        if ast is None:
            return {"module": os.path.basename(file_path), "error": "Ошибка парсинга"}
        
        # Собираем статистику
        statistics = collect_statistics(ast)
        
        violations = []
        if rules:
            rule_checker = RuleCheckingVisitor(rules)
            ast.accept(rule_checker)
            violations = rule_checker.violations
        
        return {
            "module": os.path.basename(file_path),
            "file_path": file_path,
            "statistics": statistics,
            "violations": [
                {
                    "rule_code": v.rule_code,
                    "rule_name": v.rule_name,
                    "severity": v.severity,
                    "line": v.line,
                    "column": v.column,
                    "message": v.message
                } for v in violations
            ]
        }
    except Exception as e:
        print(f"  Ошибка анализа {file_path}: {e}")
        return {
            "module": os.path.basename(file_path),
            "error": f"Ошибка анализа: {str(e)}"
        }

@app.route("/api/analyze", methods=["POST"])
def analyze_zip():
    print("\n" + "=" * 60)
    print("ПОЛУЧЕН ЗАПРОС НА /api/analyze")
    print("=" * 60)
    
    try:
        # Получаем сырые данные
        zip_data = request.get_data()
        
        if not zip_data:
            print("❌ Нет данных в запросе")
            return json_unicode({"error": "Файл не загружен"}, 400)
        
        print(f"✅ Получено {len(zip_data)} байт")
        
        # Проверяем сигнатуру ZIP файла (PK)
        if len(zip_data) < 4 or zip_data[:4] != b'PK\x03\x04':
            print(f"❌ Данные не являются ZIP-архивом")
            # Выводим первые байты для отладки
            print(f"   Первые байты: {zip_data[:20]}")
            return json_unicode({"error": "Файл должен быть ZIP-архивом"}, 400)
        
        print("✅ ZIP-архив распознан")
        
        # Распаковываем архив
        extracted_files = extract_bsl_files_from_zip(zip_data, TEMP_EXTRACT_DIR)
        
        if not extracted_files:
            print("❌ В архиве не найдено .bsl-файлов")
            return json_unicode({"error": "В архиве не найдено .bsl-файлов"}, 400)
        
        print(f"\n📁 Найдено .bsl-файлов: {len(extracted_files)}")
        for f in extracted_files:
            print(f"   - {os.path.basename(f)}")
        
        # Анализируем каждый .bsl-файл
        analysis_results = []
        total_violations = 0
        
        for bsl_file in extracted_files:
            print(f"\n🔍 Анализируем: {os.path.basename(bsl_file)}")
            result = analyze_bsl_file(bsl_file)
            analysis_results.append(result)
            
            violations_count = len(result.get("violations", []))
            total_violations += violations_count
            print(f"   Нарушений: {violations_count}")
        
        # Выводим общую статистику
        print("\n" + "=" * 60)
        print("РЕЗУЛЬТАТЫ АНАЛИЗА")
        print("=" * 60)
        print(f"Всего файлов: {len(extracted_files)}")
        print(f"Всего нарушений: {total_violations}")
        print("-" * 60)
        
        for result in analysis_results:
            module_name = result.get("module", "unknown")
            violations = result.get("violations", [])
            error = result.get("error", "")
            
            if error:
                print(f"❌ {module_name}: {error}")
            else:
                print(f"📄 {module_name}: {len(violations)} нарушений")
                for v in violations:
                    print(f"   • [{v['rule_code']}] стр.{v['line']}: {v['message']}")
        
        print("=" * 60)
        
        # Формируем JSON-ответ
        result = {
            "success": True,
            "archive_name": "archive.zip",
            "analysis_date": datetime.datetime.now().isoformat(),
            "modules_analyzed": len(extracted_files),
            "total_violations": total_violations,
            "statistics": {
                "total_files": len(extracted_files),
                "total_violations": total_violations
            },
            "violations": [
                violation
                for result in analysis_results
                for violation in result.get("violations", [])
            ]
        }
        
        return json_unicode(result, 200)
        
    except Exception as e:
        print(f"\n❌ КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        return json_unicode({"error": str(e)}, 500)
    
 
  
if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        print("\n" + "=" * 60)
        print("ЗАПУСК API АНАЛИЗАТОРА КОДА 1S")
        print("=" * 60)
        print(f"Парсер готов: {parser is not None}")
        print(f"База данных подключена: {db_connected}")
        print(f"Правила загружены: {len(rules)}")
        print("\nКонечные точки:")
        print("  GET  /api/health")
        print("  POST /api/analyze")
        print("\n" + "=" * 60)
        print("Сервер запущен по адресу http://0.0.0.0:5000")
        print("=" * 60 + "\n")
    
    # HTTP (без HTTPS)
    app.run(debug=True, host="0.0.0.0", port=5000)
