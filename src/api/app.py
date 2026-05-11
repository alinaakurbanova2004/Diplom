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

from flask import render_template, request, redirect, url_for, flash
from src.rules.rule_generator import RuleGenerator
app = Flask(__name__)
CORS(app)

app.template_folder = os.path.join(current_dir, 'templates')
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
def get_module_name(file_path: str, extract_dir: str) -> str:
    """Преобразует путь в понятное имя модуля 1С."""
    relative_path = os.path.relpath(file_path, extract_dir)
    parts = relative_path.split(os.sep)
    
    # Собираем значимые части пути
    result_parts = []
    for part in parts:
        # Пропускаем служебные папки
        if part in ['Ext', 'Form', 'Forms', 'Ext', 'Module.bsl', 'ObjectModule.bsl', 'ManagerModule.bsl']:
            continue
        if part in ['Documents', 'Catalogs', 'Reports', 'Processing', 
                   'Документы', 'Справочники', 'Отчеты', 'Обработки']:
            continue
        if part and len(part) > 0 and part not in ['bsl']:
            # Убираем расширение .bsl
            if part.endswith('.bsl'):
                part = part[:-4]
            if part and part not in ['Module', 'ObjectModule', 'ManagerModule']:
                result_parts.append(part)
    
    if result_parts:
        return ".".join(result_parts)
    
    # Если не нашли, берем имя файла без расширения
    return os.path.splitext(os.path.basename(file_path))[0]

def extract_bsl_files_from_zip(zip_data: bytes, extract_dir: str) -> List[str]:
    """Распаковывает ZIP‑архив и возвращает список путей к .bsl‑файлам."""
    bsl_files = []
    
    # Очищаем папку перед распаковкой (только здесь!)
    import shutil
    if os.path.exists(extract_dir):
        shutil.rmtree(extract_dir)
    os.makedirs(extract_dir, exist_ok=True)
    
    # Преобразуем bytes в файловый объект
    with zipfile.ZipFile(io.BytesIO(zip_data), 'r') as zip_ref:
        zip_ref.extractall(extract_dir)
        for root, dirs, files in os.walk(extract_dir):
            for file in files:
                if file.endswith('.bsl'):
                    full_path = os.path.join(root, file)
                    bsl_files.append(full_path)
                    print(f"    Найден .bsl файл: {full_path}")
    
    return bsl_files
    
def parse_module_path(file_path: str, extract_dir: str) -> Dict[str, Any]:
    """
    Разбирает путь к .bsl файлу и возвращает структурированную информацию.
    """
    
    relative_path = os.path.relpath(file_path, extract_dir)
    parts = relative_path.split(os.sep)
    
    # Словарь соответствия папок типам метаданных
    metadata_map = {
        'Справочники': 'Справочник',
        'Catalog': 'Справочник',
        'Catalogs': 'Справочник',
        'Документы': 'Документ',
        'Document': 'Документ',
        'Documents': 'Документ',
        'Отчеты': 'Отчет',
        'Report': 'Отчет',
        'Reports': 'Отчет',
        'Обработки': 'Обработка',
        'Processing': 'Обработка',
        'DataProcessors': 'Обработка',
        'РегистрыСведений': 'Регистр сведений',
        'InformationRegister': 'Регистр сведений',
        'InformationRegisters': 'Регистр сведений',
        'РегистрыНакопления': 'Регистр накопления',
        'AccumulationRegister': 'Регистр накопления',
        'AccumulationRegisters': 'Регистр накопления',
        'ПланыСчетов': 'План счетов',
        'ChartOfAccounts': 'План счетов',
        'ChartsOfAccounts': 'План счетов',
        'Константы': 'Константа',
        'Constant': 'Константа',
        'Constants': 'Константа',
        'Перечисления': 'Перечисление',
        'Enumeration': 'Перечисление',
        'Enumerations': 'Перечисление',
        'БизнесПроцессы': 'Бизнес-процесс',
        'BusinessProcess': 'Бизнес-процесс',
        'BusinessProcesses': 'Бизнес-процесс',
        'Задачи': 'Задача',
        'Task': 'Задача',
        'Tasks': 'Задача',
    }
    
    # Словарь соответствия типов форм
    form_type_map = {
        'ФормаЭлемента': 'ФормаЭлемента',
        'ФормаВыбора': 'ФормаВыбора',
        'ФормаСписка': 'ФормаСписка',
        'ФормаДокумента': 'ФормаДокумента',
        'ФормаПечати': 'ФормаПечати',
        'ФормаОтчета': 'ФормаОтчета',
        'ФормаНастроек': 'ФормаНастроек',
        'ФормаВарианта': 'ФормаВарианта',
        'ФормаОбработки': 'ФормаОбработки',
        'Форма': 'Форма',
        'Form': 'Форма',
        'Forms': 'Форма',
        'Формы': 'Форма',
    }
    
    result = {
        'module_type': '',
        'metadata_type': '',
        'metadata_name': '',
        'form_name': '',
        'full_name': ''
    }
    
    filename = os.path.basename(file_path)
    
    # Проходим по частям пути ИСКЛЮЧАЯ имя файла
    for i, part in enumerate(parts):
        # Пропускаем имя файла
        if part == filename:
            continue
            
        # Определяем тип метаданных
        if part in metadata_map:
            result['metadata_type'] = metadata_map[part]
            # Ищем имя объекта (следующая часть, которая не служебная)
            for j in range(i + 1, len(parts)):
                next_part = parts[j]
                # Исключаем служебные папки и имя файла
                if next_part not in ['Ext', 'Form', 'Forms', 'Формы', filename,
                                     'ManagerModule.bsl', 'CommandModule.bsl', 'ConfigFiles']:
                    if next_part not in metadata_map:
                        result['metadata_name'] = next_part
                        break
                    else:
                        break
                break
        
        # Определяем имя формы
        if part in ['Forms', 'Формы', 'Form', 'Форма']:
            for j in range(i + 1, len(parts)):
                next_part = parts[j]
                if next_part not in ['Ext', filename]:
                    if next_part in form_type_map:
                        result['form_name'] = form_type_map[next_part]
                    else:
                        result['form_name'] = next_part
                    break
    
    # Если не нашли имя объекта, берем последнюю неслужебную часть
    if not result['metadata_name']:
        for part in reversed(parts):
            if part not in ['Ext', 'Form', 'Forms', 'Формы', 'ConfigFiles', filename,
                           'ObjectModule.bsl', 'ManagerModule.bsl', 'Module.bsl']:
                if part not in metadata_map:
                    result['metadata_name'] = part
                    break
    
    # ФОРМИРУЕМ ПОЛНОЕ ИМЯ (БЕЗ Module.bsl и МодульФормы)
    full_name_parts = []
    if result['metadata_type']:
        full_name_parts.append(result['metadata_type'])
    if result['metadata_name']:
        full_name_parts.append(result['metadata_name'])
    if result['form_name']:
        full_name_parts.append(result['form_name'])
    
    if full_name_parts:
        result['full_name'] = '.'.join(full_name_parts)
    else:
        result['full_name'] = os.path.splitext(filename)[0]
    
    # Очищаем от лишнего
    result['full_name'] = result['full_name'].replace('..', '.')
    result['full_name'] = result['full_name'].replace('.Module.bsl', '')
    result['full_name'] = result['full_name'].replace('.ObjectModule.bsl', '')
    result['full_name'] = result['full_name'].strip('.')
    
    # Выводим отладочную информацию
    print(f"  Разбор пути: {relative_path}")
    print(f"    Тип метаданных: {result['metadata_type']}")
    print(f"    Имя объекта: {result['metadata_name']}")
    print(f"    Имя формы: {result['form_name']}")
    print(f"    Полное имя: {result['full_name']}")
    
    return result

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
            result = analyze_bsl_file(bsl_file, TEMP_EXTRACT_DIR)
            analysis_results.append(result)
            
            violations_count = len(result.get("violations", []))
            total_violations += violations_count
            print(f"   Нарушений: {violations_count}")
        quality_metrics = calculate_quality_metrics(analysis_results)

        # Выводим метрики качества в консоль
        print("\n" + "=" * 60)
        print("МЕТРИКИ КАЧЕСТВА КОДА")
        print("=" * 60)
        print(f"📊 Общее количество нарушений: {quality_metrics['total_violations']}")
        print(f"📄 Общее количество строк кода: {quality_metrics['total_loc']}")
        print(f"📈 Плотность нарушений: {quality_metrics['violations_density']} на 100 строк")
        print(f"⭐ Коэффициент соблюдения стандартов: {quality_metrics['compliance_coefficient']}")
        print(f"🎯 Теоретический максимум нарушений: {quality_metrics['theoretical_max_violations']}")

        print("\n📋 Нарушения по правилам:")
        for rule_code, rule_info in quality_metrics['violations_by_rule'].items():
            print(f"   • {rule_code}: {rule_info['count']} нарушений")

        print("=" * 60)
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
        original_filename = request.headers.get('X-Filename', 'archive.zip')
        
        # Формируем JSON-ответ
        result = {
            "success": True,
            "archive_name": original_filename,
            "analysis_date": datetime.datetime.now().strftime("%d.%m.%Y %H:%M"),
            "modules_analyzed": len(extracted_files),
            "total_violations": total_violations,
            "statistics": {
                "total_files": len(extracted_files),
                "total_violations": total_violations
            },
            "quality_metrics": { 
                "total_violations": quality_metrics['total_violations'],
                "total_loc": quality_metrics['total_loc'],
                "violations_density": quality_metrics['violations_density'],
                "compliance_coefficient": quality_metrics['compliance_coefficient'],
                "theoretical_max_violations": quality_metrics['theoretical_max_violations'],
                "violations_by_rule": quality_metrics['violations_by_rule']
            },
            "violations": [
                {
                    "module": analysis_result.get("module", "unknown"),
                    "module_type": analysis_result.get("module_type", ""),
                    "metadata_type": analysis_result.get("metadata_type", ""),
                    "metadata_name": analysis_result.get("metadata_name", ""),
                    "form_name": analysis_result.get("form_name", ""),
                    "rule_code": violation["rule_code"],
                    "rule_name": violation["rule_name"],
                    "severity": violation["severity"],
                    "line": violation["line"],
                    "column": violation["column"],
                    "message": violation["message"]
                }
                for analysis_result in analysis_results
                for violation in analysis_result.get("violations", [])
            ]
        }
        
        return json_unicode(result, 200)
        
    except Exception as e:
        print(f"\n❌ КРИТИЧЕСКАЯ ОШИБКА: {e}")
        import traceback
        traceback.print_exc()
        return json_unicode({"error": str(e)}, 500)

def calculate_quality_metrics(analysis_results: List[Dict[str, Any]]) -> Dict[str, Any]:
    """
    Рассчитывает метрики качества кода на основе результатов анализа.
    
    Возвращает словарь с метриками:
    - total_violations: общее количество нарушений
    - violations_density: плотность нарушений (нарушений на 100 строк кода)
    - compliance_coefficient: коэффициент соблюдения стандартов (0-1)
    - violations_by_rule: количество нарушений по каждому правилу
    - violations_by_module: количество нарушений по каждому модулю
    - total_loc: общее количество строк кода
    - theoretical_max_violations: теоретическое максимальное количество нарушений
    """
    
    # Инициализация
    total_violations = 0
    total_loc = 0
    violations_by_rule = {}
    violations_by_module = {}
    module_stats = []  # для хранения информации о каждом модуле
    
    # Собираем статистику по модулям
    for result in analysis_results:
        module_name = result.get("module", "unknown")
        module_violations = result.get("violations", [])
        module_loc = 0
        
        # Подсчет LOC (нужно добавить в analyze_bsl_file)
        statistics = result.get("statistics", {})
        module_loc = statistics.get("loc", 0)  # TODO: добавить подсчет LOC
        
        violations_count = len(module_violations)
        total_violations += violations_count
        total_loc += module_loc
        
        # Нарушения по модулям
        violations_by_module[module_name] = {
            "violations": violations_count,
            "loc": module_loc,
            "density": violations_count / module_loc if module_loc > 0 else 0
        }
        
        # Нарушения по правилам
        for violation in module_violations:
            rule_code = violation.get("rule_code", "unknown")
            if rule_code not in violations_by_rule:
                violations_by_rule[rule_code] = {
                    "count": 0,
                    "rule_name": violation.get("rule_name", ""),
                    "severity": violation.get("severity", "")
                }
            violations_by_rule[rule_code]["count"] += 1
        
        module_stats.append({
            "name": module_name,
            "violations": violations_count,
            "loc": module_loc,
            "density": violations_count / module_loc if module_loc > 0 else 0
        })
    
    # Плотность нарушений (на 100 строк кода)
    total_density = (total_violations / total_loc * 100) if total_loc > 0 else 0
    
    # Теоретическое максимальное количество нарушений
    # Оцениваем как количество правил * количество потенциальных точек проверки
    total_rules = len(rules) if rules else 1
    # Оценка V_max: среднее количество нарушений на модуль * количество модулей * коэффициент запаса
    avg_violations_per_module = total_violations / len(analysis_results) if analysis_results else 0
    theoretical_max_violations = max(total_violations * 2, len(analysis_results) * total_rules)
    
    # Коэффициент соблюдения стандартов
    compliance_coefficient = 1 - (total_violations / theoretical_max_violations) if theoretical_max_violations > 0 else 1
    compliance_coefficient = max(0, min(1, compliance_coefficient))  # ограничиваем от 0 до 1
    
    return {
        "total_violations": total_violations,
        "total_loc": total_loc,
        "violations_density": round(total_density, 2),
        "compliance_coefficient": round(compliance_coefficient, 3),
        "theoretical_max_violations": theoretical_max_violations,
        "violations_by_rule": violations_by_rule,
        "violations_by_module": violations_by_module,
        "module_stats": module_stats
    }

def analyze_bsl_file(file_path: str, extract_dir: str) -> Dict[str, Any]:
    """Анализирует один .bsl‑файл и возвращает результаты."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
        
        # Подсчет строк кода (без пустых строк)
        lines = code.split('\n')
        loc = len([line for line in lines if line.strip()])  # только непустые строки
        
        print(f"  Анализ файла: {os.path.basename(file_path)}")
        print(f"  Полный путь: {file_path}")
        print(f"  Строк кода: {loc}")
        
        # Разбираем путь к файлу
        path_info = parse_module_path(file_path, extract_dir)
        
        ast = parser.parse_string(code, os.path.basename(file_path))
        
        if ast is None:
            return {
                "module": path_info['full_name'],
                "module_type": path_info['module_type'],
                "metadata_type": path_info['metadata_type'],
                "metadata_name": path_info['metadata_name'],
                "form_name": path_info['form_name'],
                "loc": loc,  
                "error": "Ошибка парсинга"
            }
        
        statistics = collect_statistics(ast)
        statistics["loc"] = loc  
        
        violations = []
        if rules:
            rule_checker = RuleCheckingVisitor(rules)
            ast.accept(rule_checker)
            violations = rule_checker.violations
        
        return {
            "module": path_info['full_name'],
            "module_type": path_info['module_type'],
            "metadata_type": path_info['metadata_type'],
            "metadata_name": path_info['metadata_name'],
            "form_name": path_info['form_name'],
            "file_path": file_path,
            "loc": loc,
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
        path_info = parse_module_path(file_path, extract_dir)
        return {
            "module": path_info['full_name'],
            "module_type": path_info['module_type'],
            "metadata_type": path_info['metadata_type'],
            "metadata_name": path_info['metadata_name'],
            "form_name": path_info['form_name'],
            "loc": 0,  # ← ДОБАВЛЕНО
            "error": f"Ошибка анализа: {str(e)}"
        }

@app.route("/admin/rules")
def admin_rules():
    """Список всех правил"""
    from src.database.db_manager import RuleRepository
    rule_repo = RuleRepository(db)
    rules = rule_repo.get_all_rules()  # нужно добавить метод
    
    # Если метод get_all_rules не существует, временно используем RuleRegistry
    if not rules:
        from src.rules.rule_registry import RuleRegistry
        rules_data = []
        for rule in RuleRegistry.get_all_rules():
            rules_data.append({
                'id': getattr(rule, 'id', 0),
                'code': rule.code,
                'name': rule.name,
                'description': getattr(rule, 'description', ''),
                'severity': rule.severity,
                'is_active': getattr(rule, 'enabled', True)
            })
        rules = rules_data
    
    return render_template("admin/rules.html", rules=rules)


@app.route("/admin/rules/new", methods=["GET", "POST"])
def admin_rule_new():
    """Создание нового правила"""
    if request.method == "POST":
        form_data = {
            'code': request.form.get('code'),
            'name': request.form.get('name'),
            'description': request.form.get('description', ''),
            'severity': request.form.get('severity', 'WARNING'),
            'rule_type': 'custom',  # или можно определить по коду
            'max_params': int(request.form.get('max_params', 8)),
            'min_length': int(request.form.get('min_length', 3)),
            'forbidden_words': request.form.get('forbidden_words', ''),
            'camelcase_prefix': request.form.get('camelcase_prefix', ''),
            'is_active': request.form.get('is_active') == 'true'
        }
        
        # Определяем тип правила по коду
        code_prefix = form_data['code'].split('-')[0]
        if code_prefix == 'FUN':
            form_data['rule_type'] = 'max_params'
        elif code_prefix == 'VAR':
            # По имени можно определить тип
            if 'длин' in form_data['name'] or 'Length' in form_data['name']:
                form_data['rule_type'] = 'min_length'
            elif 'Camel' in form_data['name']:
                form_data['rule_type'] = 'camelcase'
            else:
                form_data['rule_type'] = 'forbidden_words'
        
        try:
            # Генерируем файл правила
            file_path = RuleGenerator.generate_rule_file(form_data)
            
            # Сохраняем в БД
            from src.database.db_manager import RuleRepository
            rule_repo = RuleRepository(db)
            # Нужно добавить метод save_rule в RuleRepository
            # Пока просто выводим путь
            flash(f"Правило {form_data['code']} создано! Файл: {file_path}")
            return redirect(url_for('admin_rules'))
        except Exception as e:
            flash(f"Ошибка создания правила: {e}")
            return redirect(url_for('admin_rule_new'))
    
    return render_template("admin/rule_form.html", rule=None)


@app.route("/admin/rules/<int:rule_id>/edit", methods=["GET", "POST"])

def admin_rule_edit(rule_id):
    from src.database.db_manager import RuleRepository
    rule_repo = RuleRepository(db)
    rule = rule_repo.get_rule_by_id(rule_id)
    
    if not rule:
        flash("Правило не найдено!")
        return redirect(url_for('admin_rules'))
    
    if request.method == "POST":
        # 1. Обновляем запись в БД
        update_data = {
            'name': request.form.get('name'),
            'description': request.form.get('description', ''),
            'severity': request.form.get('severity', 'WARNING'),
            'is_active': request.form.get('is_active') == 'true'
        }
        rule_repo.update_rule(rule_id, update_data)
        
        # 2. Обновляем параметры правила (max_params, min_length и т.д.)
        # Сохраняем параметры в таблицу rule_parameter
        rule_repo.delete_rule_parameters(rule_id)  # удаляем старые
        
        if request.form.get('max_params'):
            rule_repo.save_rule_parameter(rule_id, 'max_params', request.form.get('max_params'), 'integer')
        if request.form.get('min_length'):
            rule_repo.save_rule_parameter(rule_id, 'min_length', request.form.get('min_length'), 'integer')
        if request.form.get('forbidden_words'):
            rule_repo.save_rule_parameter(rule_id, 'forbidden_words', request.form.get('forbidden_words'), 'string')
        if request.form.get('camelcase_prefix'):
            rule_repo.save_rule_parameter(rule_id, 'camelcase_prefix', request.form.get('camelcase_prefix'), 'string')
        
        # 3. Перегенерируем файл правила
        from src.rules.rule_generator import RuleGenerator
        file_path = RuleGenerator.generate_rule_file(rule_id)  # читает параметры из БД
        
        # 4. Обновляем file_path и class_name в БД (если изменились)
        # (можно оставить как есть или перезаписать)
        
        flash(f"Правило {rule['code']} обновлено!")
        return redirect(url_for('admin_rules'))
    
    # GET: загружаем параметры правила из БД для отображения в форме
    params = rule_repo.get_parameters_for_rule(rule_id)
    param_dict = {p['param_name']: p['param_value'] for p in params}
    
    return render_template("admin/rule_form.html", rule={**rule, **param_dict})

def admin_rule_delete(rule_id):
    """Удаление правила"""
    from src.database.db_manager import RuleRepository
    rule_repo = RuleRepository(db)
    rule = rule_repo.get_rule_by_id(rule_id)
    
    if rule:
        # Удаляем файл правила
        file_path = Path(__file__).parent.parent / "rules" / rule.get('file_path', '')
        if file_path.exists():
            file_path.unlink()
        
        # Удаляем из БД
        # rule_repo.delete_rule(rule_id)
        flash(f"Правило {rule['code']} удалено!")
    
    return redirect(url_for('admin_rules'))

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