#!/usr/bin/env python
"""
Скрипт для запуска ANTLR без проблем с сетью
"""

import subprocess
import sys
import os

ANTLR_JAR = "C:/Diplom/Diplom/src/lib/antlr-4.13.2-complete.jar"
GRAMMAR_FILE = "C:/Diplom/Diplom/src/parser/BSL.g4"

# Проверяем, существует ли JAR
if not os.path.exists(ANTLR_JAR):
    print(f"❌ JAR не найден: {ANTLR_JAR}")
    print(" Скачай его"
          " с: https://www.antlr.org/download/antlr-4.13.2-complete.jar")
    sys.exit(1)

# Формируем команду
cmd = [
    "java",
    "-jar",
    ANTLR_JAR,
    "-Dlanguage=Python3",
    "-visitor",
    "-o",
    "./antlr_generated",  # папка для выходных файлов
    GRAMMAR_FILE,
]

print(f"🔍 Запуск: {' '.join(cmd)}")

# Создаём папку для выходных файлов
os.makedirs("./antlr_generated", exist_ok=True)

# Запускаем
result = subprocess.run(cmd, capture_output=True, text=True)

if result.returncode == 0:
    print("✅ ANTLR успешно сгенерировал парсер!")
    print("📁 Файлы сохранены в: ./antlr_generated/")
else:
    print(f"❌ Ошибка: {result.stderr}")
