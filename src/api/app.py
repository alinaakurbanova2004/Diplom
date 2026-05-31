#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime
import sys
import os
import io
import json
import zipfile
import shutil
from pathlib import Path
from typing import Any, Dict, List

from flask import Flask, make_response, request, render_template, redirect, url_for, flash
from flask_cors import CORS

current_dir = Path(__file__).parent
project_root = current_dir.parent.parent
sys.path.insert(0, str(project_root))

from src.parser.antlr_parser import AntlrBSLParser
from src.database.db_manager import DatabaseConnection, RuleRepository
from src.rules.loader import RuleLoader
from src.rules.rule_registry import RuleRegistry
from src.visitor.rules.rule_checking_visitor import RuleCheckingVisitor
from src.visitor.collectors import VariableCollector, FunctionCollector
from src.visitor.factory import VisitorFactory
from src.rules.rule_generator import RuleGenerator

app = Flask(__name__)
app.secret_key = 'my-secret-key-12345'
CORS(app)

app.template_folder = os.path.join(current_dir, 'templates')

# Папки для временных файлов
TEMP_EXTRACT_DIR = os.path.join(project_root, "temp_extract")
REPORTS_DIR = os.path.join(project_root, "reports")
os.makedirs(TEMP_EXTRACT_DIR, exist_ok=True)
os.makedirs(REPORTS_DIR, exist_ok=True)

# Парсер
try:
    parser = AntlrBSLParser()
    print("Парсер инициализирован")
except Exception as e:
    print(f"Ошибка парсера: {e}")
    parser = None

# База данных
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
    bsl_files = []
    if os.path.exists(extract_dir):
        shutil.rmtree(extract_dir)
    os.makedirs(extract_dir, exist_ok=True)
    
    with zipfile.ZipFile(io.BytesIO(zip_data), 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                if file.endswith('.bsl'):
                    bsl_files.append(os.path.join(root, file))
    return bsl_files

def parse_module_path(file_path: str, extract_dir: str) -> Dict[str, Any]:
    relative_path = os.path.relpath(file_path, extract_dir)
    parts = relative_path.split(os.sep)
    
    metadata_map = {
        'Справочники': 'Справочник', 'Catalog': 'Справочник', 'Catalogs': 'Справочник',
        'Документы': 'Документ', 'Document': 'Документ', 'Documents': 'Документ',
        'Отчеты': 'Отчет', 'Report': 'Отчет', 'Reports': 'Отчет',
        'Обработки': 'Обработка', 'Processing': 'Обработка', 'DataProcessors': 'Обработка',
        'РегистрыСведений': 'Регистр сведений', 'InformationRegister': 'Регистр сведений',
        'РегистрыНакопления': 'Регистр накопления', 'AccumulationRegister': 'Регистр накопления',
        'ПланыСчетов': 'План счетов', 'ChartOfAccounts': 'План счетов',
        'Константы': 'Константа', 'Constant': 'Константа',
        'Перечисления': 'Перечисление', 'Enumeration': 'Перечисление',
        'БизнесПроцессы': 'Бизнес-процесс', 'BusinessProcess': 'Бизнес-процесс',
        'Задачи': 'Задача', 'Task': 'Задача'
    }
    
    result = {'module_type': '', 'metadata_type': '', 'metadata_name': '', 'form_name': '', 'full_name': ''}
    filename = os.path.basename(file_path)
    
    for i, part in enumerate(parts):
        if part == filename:
            continue
        if part in metadata_map:
            result['metadata_type'] = metadata_map[part]
            for j in range(i + 1, len(parts)):
                next_part = parts[j]
                if next_part not in ['Ext', 'Form', 'Forms', 'Формы', filename, 'ManagerModule.bsl', 'CommandModule.bsl']:
                    if next_part not in metadata_map:
                        result['metadata_name'] = next_part
                        break
                break
        if part in ['Forms', 'Формы', 'Form', 'Форма']:
            for j in range(i + 1, len(parts)):
                next_part = parts[j]
                if next_part not in ['Ext', filename]:
                    result['form_name'] = next_part
                    break
    
    if not result['metadata_name']:
        for part in reversed(parts):
            if part not in ['Ext', 'Form', 'Forms', 'Формы', filename, 'ObjectModule.bsl', 'ManagerModule.bsl', 'Module.bsl']:
                if part not in metadata_map:
                    result['metadata_name'] = part
                    break
    
    full_name_parts = []
    if result['metadata_type']:
        full_name_parts.append(result['metadata_type'])
    if result['metadata_name']:
        full_name_parts.append(result['metadata_name'])
    if result['form_name']:
        full_name_parts.append(result['form_name'])
    
    result['full_name'] = '.'.join(full_name_parts) if full_name_parts else os.path.splitext(filename)[0]
    result['full_name'] = result['full_name'].replace('..', '.').strip('.')
    
    return result

@app.route("/api/analyze", methods=["POST"])
def analyze_zip():
    print("\n=== ПОЛУЧЕН ЗАПРОС НА /api/analyze ===")
    try:
        zip_data = request.get_data()
        if not zip_data:
            return json_unicode({"error": "Файл не загружен"}, 400)
        
        if len(zip_data) < 4 or zip_data[:4] != b'PK\x03\x04':
            return json_unicode({"error": "Файл должен быть ZIP-архивом"}, 400)
        
        extracted_files = extract_bsl_files_from_zip(zip_data, TEMP_EXTRACT_DIR)
        if not extracted_files:
            return json_unicode({"error": "В архиве не найдено .bsl-файлов"}, 400)
        
        analysis_results = []
        total_violations = 0
        
        for bsl_file in extracted_files:
            result = analyze_bsl_file(bsl_file, TEMP_EXTRACT_DIR)
            analysis_results.append(result)
            total_violations += len(result.get("violations", []))
        
        quality_metrics = calculate_quality_metrics(analysis_results)
        
        result = {
            "success": True,
            "archive_name": request.headers.get('X-Filename', 'archive.zip'),
            "analysis_date": datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),
            "modules_analyzed": len(extracted_files),
            "total_violations": total_violations,
            "statistics": {"total_files": len(extracted_files), "total_violations": total_violations},
            "quality_metrics": quality_metrics,
            "violations": [
                {
                    "module": r.get("module", "unknown"),
                    "module_type": r.get("module_type", ""),
                    "metadata_type": r.get("metadata_type", ""),
                    "metadata_name": r.get("metadata_name", ""),
                    "form_name": r.get("form_name", ""),
                    "rule_code": v["rule_code"],
                    "rule_name": v["rule_name"],
                    "severity": v["severity"],
                    "line": v["line"],
                    "column": v["column"],
                    "message": v["message"]
                }
                for r in analysis_results
                for v in r.get("violations", [])
            ]
        }
        return json_unicode(result, 200)
    except Exception as e:
        return json_unicode({"error": str(e)}, 500)

def calculate_quality_metrics(analysis_results):
    total_violations = sum(len(r.get("violations", [])) for r in analysis_results)
    total_loc = sum(r.get("loc", 0) for r in analysis_results)
    violations_by_rule = {}
    for r in analysis_results:
        for v in r.get("violations", []):
            code = v["rule_code"]
            violations_by_rule[code] = violations_by_rule.get(code, 0) + 1
    
    total_density = (total_violations / total_loc * 100) if total_loc > 0 else 0
    total_rules = len(rules) if rules else 1
    theoretical_max = max(total_violations * 2, len(analysis_results) * total_rules)
    compliance = 1 - (total_violations / theoretical_max) if theoretical_max > 0 else 1
    
    return {
        "total_violations": total_violations,
        "total_loc": total_loc,
        "violations_density": round(total_density, 2),
        "compliance_coefficient": round(compliance, 3),
        "theoretical_max_violations": theoretical_max,
        "violations_by_rule": violations_by_rule
    }

def analyze_bsl_file(file_path: str, extract_dir: str):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        loc = len([line for line in code.split('\n') if line.strip()])
        path_info = parse_module_path(file_path, extract_dir)
        
        ast = parser.parse_string(code, os.path.basename(file_path))
        if ast is None:
            return {**path_info, "loc": loc, "error": "Ошибка парсинга", "violations": []}
        
        statistics = collect_statistics(ast)
        statistics["loc"] = loc
        
        violations = []
        if rules:
            rule_checker = RuleCheckingVisitor(rules)
            ast.accept(rule_checker)
            violations = [{
                "rule_code": v.rule_code,
                "rule_name": v.rule_name,
                "severity": v.severity,
                "line": v.line,
                "column": v.column,
                "message": v.message
            } for v in rule_checker.violations]
        
        return {**path_info, "loc": loc, "statistics": statistics, "violations": violations}
    except Exception as e:
        return {**parse_module_path(file_path, extract_dir), "loc": 0, "error": str(e), "violations": []}

# ==================== АДМИН-ПАНЕЛЬ ====================

@app.route("/admin/rules")
def admin_rules():
    rule_repo = RuleRepository(db)
    rules_data = rule_repo.get_all_rules()
    
    # ✅ Для каждого правила загружаем параметры и форматируем описание
    for rule in rules_data:
        rule_id = rule['id']
        code = rule['code']
        
        # Загружаем параметры для правила
        params = rule_repo.get_parameters_for_rule(rule_id)
        param_dict = {}
        for p in params:
            value = int(p['param_value']) if p['param_type'] == 'integer' else p['param_value']
            param_dict[p['param_name']] = value
        
        # Форматируем описание в зависимости от кода правила
        if code == 'FUN-03' and 'max_lines' in param_dict:
            rule['description'] = f"Процедура должна содержать не более {param_dict['max_lines']} строк."
        
        elif code == 'FUN-04':
            max_total = param_dict.get('max_total_params', 7)
            max_default = param_dict.get('max_default_params', 3)
            rule['description'] = f"Функция/процедура должна иметь не более {max_total} параметров, из них не более {max_default} со значениями по умолчанию."
        
        elif code == 'VAR-04' and 'min_length' in param_dict:
            rule['description'] = f"Имена переменных должны быть длиннее {param_dict['min_length']} символов (исключение: счетчики циклов)."
        
        # Для остальных правил оставляем описание из БД
    
    return render_template("admin/rules.html", rules=rules_data)

@app.route("/admin/rules/new", methods=["GET", "POST"])
def admin_rule_new():
    if request.method == "POST":
        form_data = {
            'code': request.form.get('code'),
            'name': request.form.get('name'),
            'description': request.form.get('description', ''),
            'severity': request.form.get('severity', 'WARNING'),
            'is_active': request.form.get('is_active') == 'true'
        }
        try:
            from src.rules.rule_generator import RuleGenerator
            file_path = RuleGenerator.generate_rule_file(form_data)
            flash(f"Правило {form_data['code']} создано! Файл: {file_path}")
            return redirect(url_for('admin_rules'))
        except Exception as e:
            flash(f"Ошибка создания правила: {e}")
            return redirect(url_for('admin_rule_new'))
    return render_template("admin/rule_form.html", rule=None)

@app.route("/admin/rules/<int:rule_id>/edit", methods=["GET", "POST"])
def admin_rule_edit(rule_id):
    rule_repo = RuleRepository(db)
    rule = rule_repo.get_rule_by_id(rule_id)
    
    if not rule:
        return redirect(url_for('admin_rules'))
    
    if request.method == "POST":
        # Обновляем основную информацию
        name = request.form.get('name', '').strip()
        if not name:
            flash("Ошибка: название правила не может быть пустым!")
            return redirect(url_for('admin_rule_edit', rule_id=rule_id))
        
        # Получаем описание из формы (оно может быть изменено пользователем)
        description = request.form.get('description', '')
        
        update_data = {
            'name': name,
            'description': description,
            'severity': request.form.get('severity', 'WARNING'),
            'is_active': request.form.get('is_active') == 'true'
        }
        rule_repo.update_rule(rule_id, update_data)
        
        # Обновляем параметры
        for key, value in request.form.items():
            if key in ['name', 'description', 'severity', 'is_active']:
                continue
            if value and str(value).strip():
                param_type = 'integer' if key in ['max_total_params', 'max_default_params', 'min_length', 'max_lines'] else 'string'
                
                existing = rule_repo.db.execute_query(
                    "SELECT id FROM rule_parameter WHERE rule_id = %s AND param_name = %s",
                    (rule_id, key)
                )
                if existing:
                    rule_repo.db.execute_non_query(
                        "UPDATE rule_parameter SET param_value = %s, param_type = %s WHERE rule_id = %s AND param_name = %s",
                        (str(value).strip(), param_type, rule_id, key)
                    )
                else:
                    rule_repo.save_rule_parameter(rule_id, key, str(value).strip(), param_type)
        
        flash(f"Правило {rule['code']} обновлено!")
        return redirect(url_for('admin_rules'))
    
    # GET: загружаем параметры
    params = rule_repo.get_parameters_for_rule(rule_id)
    for p in params:
        value = int(p['param_value']) if p['param_type'] == 'integer' else p['param_value']
        rule[p['param_name']] = value
    
    print(f"\n🔍 Параметры для {rule['code']}: {dict(rule)}")
    
    # ✅ ФОРМИРУЕМ ОПИСАНИЕ ДЛЯ КОНКРЕТНЫХ ПРАВИЛ
    code = rule['code']
    
    if code == 'FUN-03':
        max_lines = rule.get('max_lines', 50)
        rule['description'] = f"Процедура должна содержать не более {max_lines} строк."
    
    elif code == 'FUN-04':
        max_total = rule.get('max_total_params', 7)
        max_default = rule.get('max_default_params', 3)
        rule['description'] = f"Функция/процедура должна иметь не более {max_total} параметров, из них не более {max_default} со значениями по умолчанию."
    
    elif code == 'VAR-04':
        min_length = rule.get('min_length', 2)
        rule['description'] = f"Имена переменных должны быть длиннее {min_length} символов (исключение: счетчики циклов)."
    
    # Для остальных правил оставляем описание как есть (из БД)
    
    return render_template("admin/rule_form.html", rule=rule)

@app.route("/admin/rules/<int:rule_id>/toggle", methods=["POST"])
def admin_rule_toggle(rule_id):
    rule_repo = RuleRepository(db)
    rule = rule_repo.get_rule_by_id(rule_id)
    if rule:
        new_status = not rule.get('is_active', True)
        rule_repo.toggle_rule_status(rule_id, new_status)
        RuleGenerator.generate_rule_file_by_id(rule_id, db)
    return redirect(url_for('admin_rules'))

@app.route("/admin/rules/<int:rule_id>/delete", methods=["POST"])
def admin_rule_delete(rule_id):
    rule_repo = RuleRepository(db)
    rule = rule_repo.get_rule_by_id(rule_id)
    if rule:
        file_path = Path(__file__).parent.parent / "rules" / rule.get('file_path', '')
        if file_path.exists():
            file_path.unlink()
        rule_repo.delete_rule(rule_id)
        flash(f"Правило {rule['code']} удалено!")
    return redirect(url_for('admin_rules'))

if __name__ == "__main__":
    print("\n" + "=" * 60)
    print("ЗАПУСК API АНАЛИЗАТОРА КОДА 1S")
    print("=" * 60)
    print(f"Парсер готов: {parser is not None}")
    print(f"База данных подключена: {db_connected}")
    print(f"Правила загружены: {len(rules)}")
    print("\nДоступные эндпоинты:")
    print("  GET  /api/health")
    print("  POST /api/analyze")
    print("  GET  /admin/rules")
    print("=" * 60)
    app.run(debug=True, host="0.0.0.0", port=5000)