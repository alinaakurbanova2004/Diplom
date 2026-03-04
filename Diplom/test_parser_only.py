import sys
from pathlib import Path
import os

# Импортируем парсер
from src.parser.bsl_parser import BSLParser

# Добавляем путь к проекту
project_root = str(Path(__file__).parent)
sys.path.insert(0, project_root)
print(f"Корень проекта: {project_root}")


# Путь к JAR-файлу
JAR_PATH = project_root + "/src/lib/bsl-language-server-0.17.0-exec.jar"

print("=" * 60)
print("🔍 ТЕСТ 1: ПРОВЕРКА ПАРСЕРА")
print("=" * 60)

# 1. Проверяем, существует ли JAR-файл

if not os.path.exists(JAR_PATH):
    print(f"JAR-файл не найден: {JAR_PATH}")
    print("   Проверь путь к файлу!")
    sys.exit(1)
else:
    print(f"JAR-файл найден: {JAR_PATH}")

# 2. Создаём парсер
try:
    parser = BSLParser(JAR_PATH)
    print("Парсер создан успешно")
except Exception as e:
    print(f"Ошибка создания парсера: {e}")
    sys.exit(1)

# 3. Тестовые примеры кода
test_codes = [
    {
        "name": "Пустая процедура",
        "code": """
Процедура Тест()
    
КонецПроцедуры
        """,
    },
    {
        "name": "Процедура с сообщением",
        "code": """
Процедура Привет()
    Сообщить("Здравствуй, мир!");
КонецПроцедуры
        """,
    },
    {
        "name": "Функция с параметрами",
        "code": """
Функция Сложить(А, Б)
    Возврат А + Б;
КонецФункции
        """,
    },
]

# 4. Тестируем парсер
print("\n" + "=" * 60)
print("ЗАПУСК ТЕСТОВ ПАРСЕРА")
print("=" * 60)

for i, test in enumerate(test_codes, 1):
    print(f"\nТЕСТ {i}: {test['name']}")
    print("-" * 40)

    try:
        ast = parser.parse_string(test["code"], f"test{i}.bsl")
        print("Модуль распарсен")
        print(f"Имя модуля: {ast.name}")
        print(f"Переменных: {len(ast.variables)}")
        print(f"Функций: {len(ast.functions)}")
        print(f"Процедур: {len(ast.procedures)}")
    except Exception as e:
        print(f"ОШИБКА: {e}")
        import traceback

        traceback.print_exc()

print("\n" + "=" * 60)
print("ТЕСТИРОВАНИЕ ПАРСЕРА ЗАВЕРШЕНО")
print("=" * 60)
