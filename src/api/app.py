#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import os
import json
from pathlib import Path
from typing import Any, Dict, List

from flask import Flask, make_response, request
from flask_cors import CORS

current_dir = Path(__file__).parent
project_root = current_dir.parent.parent
sys.path.insert(0, str(project_root))

from src.parser.antlr_parser import AntlrBSLParser
from src.database.db_manager import DatabaseConnection, ModuleRepository, ViolationRepository
from src.rules.loader import RuleLoader
from src.rules.rule_registry import RuleRegistry
from src.rules.base_rule import Violation
from src.visitor.rules.rule_checking_visitor import RuleCheckingVisitor
from src.visitor.collectors import VariableCollector, FunctionCollector
from src.visitor.factory import VisitorFactory

app = Flask(__name__)
CORS(app)

REPORTS_DIR = os.path.join(project_root, "reports")
os.makedirs(REPORTS_DIR, exist_ok=True)

try:
    parser = AntlrBSLParser()
    print("Parser initialized")
except Exception as e:
    print(f"Parser error: {e}")
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

reports_storage: Dict[str, Dict[str, Any]] = {}

rules = []
if db_connected:
    rule_loader = RuleLoader(db)
    rules = rule_loader.load_all_rules()
    RuleRegistry.register_many(rules)
    print(f"Loaded {len(rules)} rules from database")
else:
    print("Database not available")

def json_unicode(data, status=200):
    response = make_response(json.dumps(data, ensure_ascii=False, indent=2), status)
    response.headers["Content-Type"] = "application/json; charset=utf-8"
    return response

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

@app.route("/api/health", methods=["GET"])
def health_check():
    return json_unicode({
        "status": "ok",
        "parser_ready": parser is not None,
        "db_connected": db_connected,
        "rules_loaded": len(rules)
    }, 200)

@app.route("/api/rules", methods=["GET"])
def get_rules():
    rules_list = []
    for rule in rules:
        rules_list.append({
            "code": rule.code,
            "name": rule.name,
            "description": rule.description,
            "severity": rule.severity
        })
    return json_unicode({"total": len(rules_list), "rules": rules_list}, 200)

@app.route("/api/analyze/code", methods=["POST"])
def analyze_code():
    try:
        data = request.get_json()
        if not data or "code" not in data:
            return json_unicode({"error": "No code provided"}, 400)

        code = data["code"]
        module_name = data.get("module_name", "module.bsl")

        if parser is None:
            return json_unicode({"error": "Parser not initialized"}, 500)

        ast = parser.parse_string(code, module_name)
        if ast is None:
            return json_unicode({"error": "Parse error"}, 400)

        module_id = None
        if db_connected:
            module_repo = ModuleRepository(db)
            module_id = module_repo.save_module(module_name)
            print(f"Module saved: {module_name} (id={module_id})")

        statistics = collect_statistics(ast)

        violations = []
        if rules:
            rule_checker = RuleCheckingVisitor(rules)
            ast.accept(rule_checker)
            violations = rule_checker.violations

        if db_connected and violations:
            violation_repo = ViolationRepository(db)
            saved_count = 0
            for v in violations:
                rule = RuleRegistry.get_rule(v.rule_code)
                if rule:
                    violation_repo.save_violation(v, rule.id, module_id)
                    saved_count += 1
                else:
                    print(f"Rule {v.rule_code} not found in registry")
            print(f"Saved {saved_count}/{len(violations)} violations to DB")

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

        return json_unicode(result, 200)

    except Exception as e:
        return json_unicode({"error": str(e)}, 500)

@app.route("/api/analyze/file", methods=["POST"])
def analyze_file():
    try:
        if "file" not in request.files:
            return json_unicode({"error": "No file uploaded"}, 400)

        file = request.files["file"]
        if not file.filename.endswith(".bsl"):
            return json_unicode({"error": "File must be .bsl"}, 400)

        code = file.read().decode("utf-8")

        if parser is None:
            return json_unicode({"error": "Parser not initialized"}, 500)

        ast = parser.parse_string(code, file.filename)
        if ast is None:
            return json_unicode({"error": "Parse error"}, 400)

        statistics = collect_statistics(ast)

        if rules:
            rule_checker = RuleCheckingVisitor(rules)
            ast.accept(rule_checker)
            violations = rule_checker.violations
        else:
            violations = []

        result = {
            "success": True,
            "module_name": file.filename,
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

        return json_unicode(result, 200)

    except Exception as e:
        return json_unicode({"error": str(e)}, 500)

@app.route("/api/reports/<report_id>", methods=["GET"])
def get_report(report_id: str):
    try:
        if report_id in reports_storage:
            return json_unicode(reports_storage[report_id], 200)

        file_path = os.path.join(REPORTS_DIR, f"{report_id}.json")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            return json_unicode(data, 200)

        return json_unicode({"error": "Report not found"}, 404)

    except Exception as e:
        return json_unicode({"error": str(e)}, 500)

@app.errorhandler(404)
def not_found(error):
    return json_unicode({"error": "Endpoint not found"}, 404)

@app.errorhandler(500)
def internal_error(error):
    return json_unicode({"error": "Internal server error"}, 500)

if __name__ == "__main__":
    if os.environ.get("WERKZEUG_RUN_MAIN") != "true":
        print("\n" + "=" * 60)
        print("STARTING 1S CODE ANALYZER API")
        print("=" * 60)
        print(f"Parser ready: {parser is not None}")
        print(f"Database connected: {db_connected}")
        print(f"Rules loaded: {len(rules)}")
        print("\nEndpoints:")
        print("  GET  /api/health")
        print("  GET  /api/rules")
        print("  POST /api/analyze/code")
        print("  POST /api/analyze/file")
        print("  GET  /api/reports/<id>")
        print("\n" + "=" * 60)
        print("Server running on http://127.0.0.1:5000")
        print("=" * 60 + "\n")

    app.run(debug=True, host="0.0.0.0", port=5000)