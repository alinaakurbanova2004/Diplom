#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Простой тест правил анализа
"""

import sys
from pathlib import Path
from src.parser.antlr_parser import AntlrBSLParser
from src.rules.registry import RuleRegistry
from src.visitor.rules.rule_checking_visitor import RuleCheckingVisitor

# Добавляем путь к проекту
project_root = str(Path(__file__).parent)
sys.path.insert(0, project_root)


# Создаём парсер и загружаем правила
parser = AntlrBSLParser()
rules = RuleRegistry.get_all_rules()

print("=" * 60)
print("🧪 ТЕСТИРОВАНИЕ ПРАВИЛ АНАЛИЗА")
print("=" * 60)
print(f"📋 Загружено правил: {len(rules)}")

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
        "expected_rules": [],  # никаких правил не должно сработать
    },
    {
        "name": "Нарушения именования (VAR-01, VAR-02, VAR-04)",
        "code": """
Перем x;                // одна буква
Перем _счетчик;         // подчеркивание в начале
Перем кол;              // сокращение
Перем ПЛОХОЕИМЯ;        // все заглавные

Процедура Тест()
    Перем т;             // одна буква
КонецПроцедуры
""",
        "expected_rules": ["VAR-01", "VAR-02", "VAR-04"],
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
        "name": "Запрос в цикле (PERF-01)",
        "code": """
Процедура Плохая()
    Для Индекс = 1 По 10 Цикл
        Запрос = Новый Запрос;
        Запрос.Текст = "ВЫБРАТЬ * ИЗ Справочник.Товары";
        Результат = Запрос.Выполнить();
    КонецЦикла;
КонецПроцедуры
""",
        "expected_rules": ["PERF-01"],
    },
]

# Запускаем тесты
for i, test in enumerate(test_cases, 1):
    print(f"\n{'='*60}")
    print(f"🧪 ТЕСТ {i}: {test['name']}")
    print(f"{'='*60}")

    # Парсим код
    # module = parser.parse_string(test["code"], f"test{i}.bsl")
    module = parser.parse_file("test.bsl")
    if not module:
        print("❌ Ошибка парсинга!")
        continue

    # Применяем правила
    rule_checker = RuleCheckingVisitor(rules)
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
