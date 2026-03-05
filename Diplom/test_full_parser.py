from src.parser.antlr_parser import AntlrBSLParser

parser = AntlrBSLParser()

# Тест 1: Простые объявления
code1 = """
Перем Счетчик Экспорт;
Перем Временная;

Функция Сложить(А, Б)
    Возврат А + Б;
КонецФункции

Процедура Тест(Парам)
    Сообщить(Парам);
КонецПроцедуры
"""

# Тест 2: Условные операторы
code2 = """
Функция Проверить(Знач Число)
    Если Число > 0 Тогда
        Возврат Истина;
    Иначе
        Возврат Ложь;
    КонецЕсли;
КонецФункции
"""

# Тест 3: Циклы
code3 = """
Процедура Посчитать(Знач N)
    Сумма = 0;
    Для Сч = 1 По N Цикл
        Сумма = Сумма + Сч;
    КонецЦикла;
    Сообщить(Сумма);
КонецПроцедуры
"""

# Тест 4: Сложные выражения
code4 = """
Функция Вычислить(А, Б, В)
    Результат = (А + Б) * В / 2;
    Возврат Результат;
КонецФункции
"""

# Тест 5: Вложенные функции и вызовы
code5 = """
Функция Внутренняя(Х)
    Возврат Х * 2;
КонецФункции

Процедура Внешняя()
    Результат = Внутренняя(5);
    Сообщить(Результат);
КонецПроцедуры
"""

code6 = """
Перем ГлобальныйСчетчик Экспорт;

Процедура Тест()
    Перем ЛокальнаяПеременная;
    ЛокальнаяПеременная = 5;
КонецПроцедуры
"""
test_cases = [
    ("Простые объявления", code1),
    ("Условные операторы", code2),
    ("Циклы", code3),
    ("Сложные выражения", code4),
    ("Вложенные функции", code5),
    ("Глобальные и локальные переменные", code6)
]

for name, code in test_cases:
    print(f"\n{'='*60}")
    print(f"🧪 ТЕСТ: {name}")
    print(f"{'='*60}")

    module = parser.parse_string(code, f"{name}.bsl")

    if module:
        print("Успешно!")
    
        # ===== ГЛОБАЛЬНЫЕ ПЕРЕМЕННЫЕ =====
        print(f"\nГлобальные переменные: {len(module.variables)}")
        if module.variables:
            for i, var in enumerate(module.variables, 1):
                экспорт = " (Экспорт)" if var.is_export else ""
                print(f"   {i}. {var.name}{экспорт}")
        else:
            print(" Глобальных переменных нет")
    
        # ===== ФУНКЦИИ =====
        print(f"\n Функции: {len(module.functions)}")
        for func in module.functions:
            print(f"\n   Функция '{func.name}':")
            print(f"      Параметров: {len(func.parameters)}")
            for param in func.parameters:
                знач = " (по значению)" if param.by_value else ""
                print(f"         - {param.name}{знач}")
        
            # Локальные переменные функции
            print(f"      Локальных переменных: {len(func.local_vars)}")
            for var in func.local_vars:
                print(f"         - {var.name}")
    
        # ===== ПРОЦЕДУРЫ =====
        print(f"\n Процедуры: {len(module.procedures)}")
        for proc in module.procedures:
            print(f"\n   Процедура '{proc.name}':")
            print(f"      Параметров: {len(proc.parameters)}")
            for param in proc.parameters:
                знач = " (по значению)" if param.by_value else ""
                print(f"         - {param.name}{знач}")
        
            # Локальные переменные процедуры
            print(f"      Локальных переменных: {len(proc.local_vars)}")
            for var in proc.local_vars:
                print(f"         - {var.name}")

    else:
        print("❌ Ошибка парсинга!")