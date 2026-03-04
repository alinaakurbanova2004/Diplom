from src.parser.antlr_parser import AntlrBSLParser

code = """Перем Счетчик Экспорт;

Процедура Тест(Парам1, Парам2)
    Сообщить("Привет, " + Парам1);
КонецПроцедуры

Функция Сумма(А, Б)
    Тест("внутри функции", А);
    Возврат А + Б;
КонецФункции

"""

parser = AntlrBSLParser()
module = parser.parse_string(code, "test.bsl")

if module:
    print(f"✅ Модуль: {module.name}")
    print(f"   Переменных: {len(module.variables)}")
    print(f"   Процедур: {len(module.procedures)}")
    print(f"   Функций: {len(module.functions)}")
else:
    print("❌ Модуль не создан")
