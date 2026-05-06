from antlr4 import InputStream, CommonTokenStream
from src.parser.antlr.BSLLexer import BSLLexer
from src.parser.antlr.BSLParser import BSLParser
from src.parser.antlr_to_ast import AntlrToAST
from src.parser.ast_nodes import ModuleNode

from antlr4.error.ErrorListener import ErrorListener


class CustomErrorListener(ErrorListener):
    """Кастомный обработчик ошибок ANTLR"""

    def __init__(self):
        self.errors = []

    def syntaxError(self, recognizer, offendingSymbol, line, column, msg, e):
        error_msg = f"Синтаксическая ошибка в {line}:{column} - {msg}"
        print(error_msg)
        self.errors.append(error_msg)


class AntlrBSLParser:
    """Парсер для языка 1С на основе ANTLR"""

    def parse_string(self, code: str,
                     module_name: str = "module.bsl") -> ModuleNode:
        print(f"📝 Парсинг модуля: {module_name}")
        print(f"📏 Длина кода: {len(code)} символов")
        print(f"📌 Код в repr: {repr(code)}")
        
        input_stream = InputStream(code)
        lexer = BSLLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = BSLParser(stream)
        
        # Добавляем listener для ошибок
        error_listener = CustomErrorListener()
        parser.removeErrorListeners()
        parser.addErrorListener(error_listener)

        # Получаем корневое правило
        tree = parser.bslFile()
        print("Дерево разбора получено")
        print(f"Тип дерева: {type(tree).__name__}")
        print(f"Количество детей: {tree.getChildCount()}")

        # Выведем первых несколько детей для отладки
        for i in range(min(3, tree.getChildCount())):
            child = tree.getChild(i)
            print(
                f"   Ребенок {i}: {
                    type(child).__name__} - текст: '{child.getText()}'"
            )

        if error_listener.errors:
            print(f"❌ Найдено {
                len(error_listener.errors)} синтаксических ошибок")
            for err in error_listener.errors:
                print(f"   {err}")
            return None

        print("🔄 Запуск визитора...")
        visitor = AntlrToAST()

        try:
            module = visitor.visit(tree)
            print(f"📦 Результат визитора: {module}")
        except Exception as e:
            print(f"❌ Ошибка в визиторе: {e}")
            import traceback

            traceback.print_exc()
            return None

        if module is None:
            print("❌ Визитор вернул None")
            if hasattr(visitor, "errors") and visitor.errors:
                print("   Ошибки визитора:")
                for err in visitor.errors:
                    print(f"   - {err}")
            return None

        module.name = module_name
        module.source_file = module_name
        print(f"✅ Модуль успешно создан: {module.name}")
        return module

    def parse_file(self, file_path: str) -> ModuleNode:
        """Парсит файл .bsl"""
        with open(file_path, "r", encoding="utf-8") as f:
            code = f.read()
        module = self.parse_string(code, file_path)
        module.source_file = file_path
        return module
