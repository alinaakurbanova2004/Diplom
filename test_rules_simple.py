#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Простой тест правил анализа
"""

import os
import sys
import tempfile
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
    
    // 2. Нарушение - два оператора в одной строке
    Сумма = 0; Результат = 5;
    
    // 3. Нарушение - три оператора
    А = 1; Б = 2; В = 3;
    
    // 4. Смешанный случай - присваивание и вызов процедуры
    Х = 10; Сообщить(Х);
    
    // 5. Операторы в цикле
    Для Индекс = 1 По 5 Цикл
        // Правильно - по одному на строку
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
    with tempfile.NamedTemporaryFile(mode='w', suffix='.bsl', encoding='utf-8', delete=False) as tmp:
        tmp.write(test["code"])
        tmp_path = tmp.name

    try:
        # Парсим файл
        module = parser.parse_file(tmp_path)
        
        print("\n🔍 Отладка AST:")
        print(f"   Глобальных переменных: {len(module.variables)}")
        for proc in module.procedures:
            print(f"   Процедура '{proc.name}':")
            print(f"      Локальных переменных: {len(proc.local_vars)}")
            for var in proc.local_vars:
                print(f"         - {var.name}")
            
        if not module:
            print("❌ Ошибка парсинга!")
            continue
        # Перед применением правил
        print(f"\n📊 Статистика правил FUN-04:")
        fun04_rules = [r for r in rules if r.code == 'FUN-04']
        print(f"   Количество экземпляров FUN-04 в списке: {len(fun04_rules)}")
        
        # Применяем правила
        rule_checker = RuleCheckingVisitor(rules)
        module.accept(rule_checker)

        violations = rule_checker.violations
        
        # После сбора нарушений
        fun04_violations = [v for v in violations if v.rule_code == 'FUN-04']
        print("\n📊 Статистика нарушений FUN-04:")
        print(f"   Всего нарушений FUN-04: {len(fun04_violations)}")
        
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
