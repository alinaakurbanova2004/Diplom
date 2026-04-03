#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Простой тест правил анализа
"""
import os
import sys
import tempfile
from pathlib import Path

# Добавляем путь к проекту
project_root = str(Path(__file__).parent)
sys.path.insert(0, project_root)

from src.parser.antlr_parser import AntlrBSLParser
from src.rules.rule_registry import RuleRegistry
from src.rules.loader import RuleLoader
from src.database.db_manager import DatabaseConnection
from src.visitor.rules.rule_checking_visitor import RuleCheckingVisitor


# ===== ПОДКЛЮЧЕНИЕ К БАЗЕ ДАННЫХ =====
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'bsl_analyzer',
    'user': 'alina',
    'password': 'pizdecqwerty1234'
}

# Подключаемся к БД
db = DatabaseConnection(**DB_CONFIG)
if not db.connect():
    print("❌ Не удалось подключиться к БД!")
    sys.exit(1)

# Загружаем правила из БД через RuleLoader
rule_loader = RuleLoader(db)
rules = rule_loader.load_all_rules()

# Регистрируем правила в RuleRegistry для быстрого доступа
RuleRegistry.register_many(rules)
print(f"✅ Загружено правил: {len(rules)}")

# Создаём парсер
parser = AntlrBSLParser()

print("=" * 60)
print("🧪 ТЕСТИРОВАНИЕ ПРАВИЛ АНАЛИЗА")
print("=" * 60)
print(f"📋 Загружено правил: {len(RuleRegistry.get_all_rules())}")

# Список тестов с описанием, какие правила должны сработать
test_cases = [
    {
        "name": "Правильные имена переменных",
        "code": """
Перем Счетчик Экспорт;
Перем ВременнаяПеременная;

Процедура Тест()
    Перем ЛокальнаяПеременная;
    ЛокальнаяПеременная = 5;
КонецПроцедуры
""",
        "expected_rules": [],
    },
    {
        "name": "Нарушения именования (VAR-01, VAR-02, VAR-03, VAR-04)",
        "code": """
Перем x;                // одна буква
Перем _счетчик;         // подчеркивание в начале
Перем кол;              // сокращение
Перем ПЛОХОЕИМЯ;        // все заглавные

Процедура Тест()
    Перем т;             // одна буква
КонецПроцедуры
""",
        "expected_rules": ["VAR-01", "VAR-02", "VAR-03", "VAR-04"],
    },
    {
        "name": "Слишком много параметров (FUN-04)",
        "code": """
Функция СлишкомМногоПараметров(П1, П2, П3, П4, П5, П6, П7, П8, П9)
    Возврат П1;
КонецФункции
""",
        "expected_rules": ["FUN-04"],
    },
    {
        "name": "Пустая процедура (FUN-02)",
        "code": """
Процедура Пустая()
    
КонецПроцедуры
""",
        "expected_rules": ["FUN-02"],
    },
    {
        "name": "Несколько операторов в строке",
        "code": """
Процедура ТестПравилаОдинОператорВСтроке()

    // 1. Правильная строка - один оператор
    Счетчик = 0;
    
    // 2. Наружение - два оператора в одной строке
    Сумма = 0; Результат = 5;
    
    // 3. Нарушение - три оператора
    А = 1; Б = 2; В = 3;
    
    // 4. Смешанный случай - присваивание и вызов процедуры
    Х = 10; Сообщить(Х);
    
    // 5. Операторы в цикле
    Для Индекс = 1 По 5 Цикл
        Элемент = Индекс;
        Сообщить(Элемент);
    КонецЦикла;
КонецПроцедуры
""",
        "expected_rules": ["VAR-01", "VAR-04", "FUN-01"],
    },
]

# Запускаем тесты
for i, test in enumerate(test_cases, 1):
    print(f"\n{'='*60}")
    print(f"🧪 ТЕСТ {i}: {test['name']}")
    print(f"{'='*60}")

    # Создаём временный файл
    with tempfile.NamedTemporaryFile(
        mode='w', suffix='.bsl', encoding='utf-8', delete=False
    ) as tmp:
        tmp.write(test["code"])
        tmp_path = tmp.name

    try:
        # Парсим файл
        module = parser.parse_file(tmp_path)
        
        if not module:
            print("❌ Ошибка парсинга!")
            continue
        
        print("\n🔍 Отладка AST:")
        print(f"   Глобальных переменных: {len(module.variables)}")
        for proc in module.procedures:
            print(f"   Процедура '{proc.name}':")
            print(f"      Локальных переменных: {len(proc.local_vars)}")
            for var in proc.local_vars:
                print(f"         - {var.name}")
        
        # Применяем правила
        rule_checker = RuleCheckingVisitor(RuleRegistry.get_all_rules())
        module.accept(rule_checker)

        violations = rule_checker.violations
        
        # Выводим результаты
        print(f"\n📊 Найдено нарушений: {len(violations)}")

        if violations:
            print("\n🔍 Список нарушений:")
            for v in violations:
                print(f"   [{v.severity}] {v.rule_code}: {v.message} (строка {v.line})")

        # Проверяем ожидаемые правила
        found_rules = {v.rule_code for v in violations}
        expected_rules = set(test["expected_rules"])

        if found_rules == expected_rules:
            print("\n✅ ТЕСТ ПРОЙДЕН! Найдены все ожидаемые правила.")
        else:
            missing = expected_rules - found_rules
            extra = found_rules - expected_rules

            print("\n❌ ТЕСТ НЕ ПРОЙДЕН!")
            if missing:
                print(f"   ❌ Не найдены: {missing}")
            if extra:
                print(f"   ⚠️ Лишние: {extra}")
    
    finally:
        os.unlink(tmp_path)

print("\n" + "=" * 60)
print("✅ ТЕСТИРОВАНИЕ ЗАВЕРШЕНО")
print("=" * 60)