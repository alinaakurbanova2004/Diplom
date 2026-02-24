import sys
import os
import json
from pathlib import Path
from typing import List, Dict, Any

# Flask и расширения
from flask import Flask, jsonify, make_response, request
from flask_cors import CORS

# Импортируем твои модули
from src.rules.violation import Violation
from src.parser.bsl_parser import BSLParser
from src.rules.registry import RuleRegistry
from src.visitor.collectors import VariableCollector, FunctionCollector
from src.visitor.factory import VisitorFactory


# Добавляем путь к проекту (чтобы видеть src)
project_root = str(Path(__file__).parent.parent)
sys.path.insert(0, project_root)
print(f"Корень проекта: {project_root}")


app = Flask(__name__)
CORS(app)  # Разрешаем запросы из браузера и 1С

# Конфигурация
JAR_PATH = os.path.join(
    project_root, "lib", "bsl-language-server-0.28.4-exec.jar")
REPORTS_DIR = os.path.join(project_root, "reports")

# Создаем папку для отчетов, если её нет
os.makedirs(REPORTS_DIR, exist_ok=True)

# Инициализируем парсер
try:
    parser = BSLParser(JAR_PATH)
    print(f"Парсер инициализирован: {JAR_PATH}")
except Exception as e:
    print(f"Ошибка инициализации парсера: {e}")
    parser = None

# Загружаем правила
try:
    rules = RuleRegistry.get_all_rules()
    print(f"Загружено правил: {len(rules)}")
except Exception as e:
    print(f"Ошибка загрузки правил: {e}")
    rules = []

reports_storage: Dict[str, Dict[str, Any]] = {}


# Для полноценного отображения на странице
def json_unicode(data, status=200):
    """Возвращает JSON с поддержкой Unicode"""
    response = make_response(json.dumps(
        data, ensure_ascii=False, indent=2), status)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response


def apply_rules_to_ast(ast) -> List[Violation]:
    """
    Применяет все правила к AST и возвращает список нарушений
    """
    from src.visitor.rules.rule_checking_visitor import RuleCheckingVisitor

    rule_checker = RuleCheckingVisitor(rules)
    ast.accept(rule_checker)
    return rule_checker.violations


def collect_statistics(ast) -> Dict[str, Any]:
    """
    Собирает статистику о модуле с помощью разных collector'ов
    """
    # Создаем collector'ы
    var_collector = VariableCollector()
    func_collector = FunctionCollector()

    # Объединяем их
    composite = VisitorFactory.create_composite_visitor(
        [var_collector, func_collector])

    # Обходим AST
    ast.accept(composite)

    return {
        "variables": {
            "total": len(var_collector.variables),
            "by_scope": (
                var_collector.get_statistics()
                if hasattr(var_collector, "get_statistics")
                else {}
            ),
        },
        "functions": {
            "total": len(func_collector.functions),
            "with_return": sum(
                1 for f in func_collector.functions if f.get(
                    "has_return", False)
            ),
            "without_return": sum(
                1 for f in func_collector.functions if not f.get(
                    "has_return", True)
            ),
        },
    }


def save_report(report_id: str, data: Dict[str, Any]) -> str:
    """
    Сохраняет отчет в файл и в память
    """
    reports_storage[report_id] = data

    # Сохраняем в файл
    file_path = os.path.join(REPORTS_DIR, f"{report_id}.json")
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    return file_path


@app.route("/api/health", methods=["GET"])
def health_check():
    """
    Проверка работоспособности сервера
    GET /api/health
    """
    return (
        jsonify(
            {
                "status": "ok",
                "timestamp": str(Path(__file__).stat().st_mtime),
                "parser_ready": parser is not None,
                "rules_loaded": len(rules),
                "version": "1.0.0",
            }
        ),
        200,
    )


@app.route("/api/rules", methods=["GET"])
def get_rules():
    """
    Возвращает список всех доступных правил
    GET /api/rules
    """
    rules_list = []
    for rule in rules:
        rules_list.append(
            {
                "code": rule.code,
                "name": rule.name,
                "description": rule.description,
                "severity": rule.severity,
            }
        )

    return json_unicode({"total": len(rules_list), "rules": rules_list}), 200


@app.route("/api/analyze/code", methods=["POST"])
def analyze_code():
    """
    Анализирует код 1С, переданный в теле запроса
    POST /api/analyze/code
    {
        "code": "Процедура Тест()\n    Сообщить(\"Привет\");\nКонецПроцедуры",
        "module_name": "test.bsl",  # опционально
        "apply_rules": true          # опционально
    }
    """
    try:
        # 1. Получаем данные из запроса
        data = request.get_json()

        if not data or "code" not in data:
            return (
                jsonify(
                    {"error": "Не передан код для анализа",
                     "code": "MISSING_CODE"}
                ),
                400,
            )

        code = data["code"]
        module_name = data.get("module_name", "module.bsl")
        apply_rules = data.get("apply_rules", True)

        # 2. Проверяем парсер
        if parser is None:
            return (
                jsonify(
                    {"error": "Парсер не инициализирован",
                     "code": "PARSER_ERROR"}),
                500,
            )

        # 3. Парсим код в AST
        ast = parser.parse_string(code, module_name)

        # 4. Собираем статистику
        statistics = collect_statistics(ast)

        # 5. Применяем правила (если нужно)
        violations = []
        if apply_rules:
            violations = apply_rules_to_ast(ast)

        # 6. Формируем результат
        result = {
            "success": True,
            "module_name": module_name,
            "statistics": statistics,
            "violations": [
                {
                    "rule_code": v.rule_code,
                    "rule_name": v.rule_name,
                    "severity": v.severity,
                    "line": v.line,
                    "column": v.column,
                    "message": v.message,
                }
                for v in violations
            ],
            "violations_count": len(violations),
        }

        return jsonify(result), 200

    except Exception as e:
        return json_unicode({"error": str(e), "code": "ANALYSIS_ERROR"}), 500


@app.route("/api/reports/<report_id>", methods=["GET"])
def get_report(report_id: str):
    """
    Получает сохраненный отчет по ID
    GET /api/reports/<report_id>
    """
    try:
        # Сначала ищем в памяти
        if report_id in reports_storage:
            return jsonify(reports_storage[report_id]), 200

        # Потом в файлах
        file_path = os.path.join(REPORTS_DIR, f"{report_id}.json")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return json_unicode(data), 200

        return (
            json_unicode(
                {"error": "Отчет не найден", "code": "REPORT_NOT_FOUND"}),
            404,
        )

    except Exception as e:
        return json_unicode({"error": str(e), "code": "REPORT_ERROR"}), 500


@app.errorhandler(404)
def not_found(error):
    """Обработка 404 ошибки"""
    return json_unicode(
        {"error": "Эндпоинт не найден",
         "code": "NOT_FOUND"}), 404


@app.errorhandler(500)
def internal_error(error):
    """Обработка 500 ошибки"""
    return (
        json_unicode(
            {"error": "Внутренняя ошибка сервера", "code": "INTERNAL_ERROR"}),
        500,
    )


# Запуск сервера

if __name__ == "__main__":
    if not app.debug or os.environ.get("WERKZEUG_RUN_MAIN") == "true":
        print("\n" + "=" * 60)
        print("ЗАПУСК REST API ДЛЯ АНАЛИЗАТОРА 1С")
        print("=" * 60)
        print(f"Корень проекта: {project_root}")
        print(f"Папка отчетов: {REPORTS_DIR}")
        print(f"Парсер готов: {parser is not None}")
        print(f"Правил загружено: {len(rules)}")
        print("\n📡 Доступные эндпоинты:")
        print("   GET  /api/health")
        print("   GET  /api/rules")
        print("   POST /api/analyze/code")
        print("   POST /api/analyze/file")
        print("   GET  /api/reports/<id>")
        print("\n" + "=" * 60)
        print("Сервер запущен на http://127.0.0.1:5000")
        print("=" * 60 + "\n")

    app.run(debug=True, host="0.0.0.0", port=5000)
