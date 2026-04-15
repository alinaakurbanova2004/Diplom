#!/usr/bin/env python3
# main.py - Анализатор без API

import sys
import json
import os
from datetime import datetime

from src.database.db_manager import ModuleRepository, ViolationRepository

# Добавляем путь к проекту
project_path = '/home/alina/Загрузки/Diplom-main/Diplom'
sys.path.insert(0, project_path)

# ПРОВЕРКА: существуют ли необходимые модули
try:
    from src.parser.antlr_parser import AntlrBSLParser
    from src.rules.loader import RuleLoader
    from src.rules.rule_registry import RuleRegistry
    from src.visitor.rules.rule_checking_visitor import RuleCheckingVisitor
    from src.visitor.collectors import VariableCollector, FunctionCollector
    from src.visitor.factory import VisitorFactory
    from src.database.db_manager import DatabaseConnection
    print("✅ Все модули загружены")
except ImportError as e:
    print(f"❌ Ошибка импорта: {e}")
    print(f"Проверьте путь: {project_path}")
    sys.exit(1)


def analyze_file(filepath: str, result_dir: str):
    """Анализирует файл и сохраняет JSON результат в result_dir"""
    
    print(f"📄 Анализ: {filepath}")
    
    # 1. Читаем файл
    with open(filepath, 'r', encoding='utf-8') as f:
        code = f.read()
    
    # 2. Парсим
    parser = AntlrBSLParser()
    ast = parser.parse_string(code, filepath)
    
    if ast is None:
        print("❌ Ошибка парсинга")
        return None
    
    # 3. Загружаем правила из БД
    DB_CONFIG = {
        'host': 'localhost',
        'port': 5432,
        'database': 'bsl_analyzer',
        'user': 'alina',
        'password': 'pizdecqwerty1234'
    }
    
    db = DatabaseConnection(**DB_CONFIG)
    db_connected = db.connect()
    
    rule_loader = RuleLoader(db)
    rules = rule_loader.load_all_rules()
    RuleRegistry.register_many(rules)
    
    # 4. Проверяем правила
    rule_checker = RuleCheckingVisitor(rules)
    ast.accept(rule_checker)
    violations = rule_checker.violations
    
    # 5. Собираем статистику
    var_collector = VariableCollector()
    func_collector = FunctionCollector()
    composite = VisitorFactory.create_composite_visitor([var_collector, func_collector])
    ast.accept(composite)
    
    module_id = None
    if db_connected and violations:
        try:
            # Сохраняем модуль
            module_repo = ModuleRepository(db)
            module_name = os.path.basename(filepath)
            module_id = module_repo.save_module(module_name, filepath)
            print(f"💾 Модуль сохранён: {module_name} (id={module_id})")
            
            # Сохраняем нарушения
            violation_repo = ViolationRepository(db)
            saved_count = 0
            for v in violations:
                rule = RuleRegistry.get_rule(v.rule_code)
                if rule and hasattr(rule, 'id'):
                    violation_repo.save_violation(v, rule.id, module_id)
                    saved_count += 1
                    print(f"   ✅ Сохранено нарушение: {v.rule_code}")
                else:
                    print(f"   ⚠️ Правило не найдено: {v.rule_code}")
            print(f"💾 Сохранено нарушений в БД: {saved_count}/{len(violations)}")
        except Exception as e:
            print(f"❌ Ошибка сохранения в БД: {e}")
            import traceback
            traceback.print_exc()

    # 6. Формируем результат
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    base_name = os.path.splitext(os.path.basename(filepath))[0]
    
    result = {
        "success": True,
        "module_name": os.path.basename(filepath),
        "analyzed_at": datetime.now().isoformat(),
        # "statistics": {
        #     "variables": {"total": len(var_collector.variables)},
        #     "functions": {"total": len(func_collector.functions)},
        #     "procedures": {"total": len(func_collector.procedures) if hasattr(func_collector, 'procedures') else 0}
        # },
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
    
    # 7. Сохраняем JSON в result_dir
    os.makedirs(result_dir, exist_ok=True)
    output_file = os.path.join(result_dir, f"{timestamp}_{base_name}.json")
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    
    print(f"✅ Результат: {output_file}")
    print(f"📊 Нарушений: {len(violations)}")
    
    return result


if __name__ == "__main__":
    DEFAULT_RESULT_DIR = "/home/alina/1c_files/result"
    
    if len(sys.argv) < 2:
        print("Использование: python main.py <файл.bsl> [папка_для_результатов]")
        print(f"Если папка не указана, используется: {DEFAULT_RESULT_DIR}")
        sys.exit(1)
    
    filepath = sys.argv[1]
    
    if len(sys.argv) > 2:
        result_dir = sys.argv[2]
    else:
        result_dir = DEFAULT_RESULT_DIR
    
    if not os.path.exists(filepath):
        print(f"❌ Файл не найден: {filepath}")
        sys.exit(1)
    
    print(f"📁 Результаты будут сохранены в: {result_dir}")
    analyze_file(filepath, result_dir)