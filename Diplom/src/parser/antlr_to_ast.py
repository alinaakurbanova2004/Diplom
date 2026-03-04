from .antlr.BSLVisitor import BSLVisitor
from .antlr.BSLParser import BSLParser
from antlr4.tree.Tree import TerminalNode
from src.parser.ast_nodes import (
    ModuleNode,
    FunctionNode,
    ProcedureNode,
    VariableNode,
    ParameterNode,
    ReturnStatementNode,
    LiteralNode,
)


class AntlrToAST(BSLVisitor):
    """Преобразует ANTLR AST в AST"""

    def __init__(self):
        self.module = None
        self.current_function = None
        self.current_procedure = None
        self.errors = []

    def visitModuleDeclaration(self, ctx):
        try:
            name = ctx.ID().getText()
            print(f"🔍 Найдено объявление модуля: {name}")

            is_export = (
                ctx.getChildCount() > 2 
                and ctx.getChild(2).getText() == "Экспорт"
            )

            var_node = VariableNode(name, is_export)
            return var_node

        except Exception as e:
            self.errors.append(f"Ошибка в модуле: {e}")
            print(f"❌ Ошибка в объявлении модуля: {e}")
            import traceback

            traceback.print_exc()
            return None

    def visitVariableDeclaration(self, ctx):
        try:
            name = ctx.ID().getText()
            print(f"🔍 Найдена переменная: {name}")

            is_export = (
                ctx.getChildCount() > 2 
                and ctx.getChild(2).getText() == "Экспорт"
            )

            var_node = VariableNode(name, is_export)
            return var_node

        except Exception as e:
            self.errors.append(f"Ошибка в переменной: {e}")
            print(f"❌ Ошибка в объявлении переменной: {e}")
            import traceback

            traceback.print_exc()
            return None

    def visitProcedure(self, ctx):
        try:
            name = ctx.ID().getText()
            proc = ProcedureNode(name)

            self.current_procedure = proc

            # Парсим параметры
            if ctx.parameterList():
                param_list = ctx.parameterList()
                for i in range(param_list.getChildCount()):
                    child = param_list.getChild(i)
                    # Проверяем, что это токен ID
                    if (
                        isinstance(child, TerminalNode)
                        and child.symbol.type == BSLParser.ID
                    ):
                        param = ParameterNode(child.getText(), False, False)
                        proc.parameters.append(param)

            # Парсим тело процедуры
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if isinstance(child, BSLParser.ReturnStatementContext):
                    stmt = self.visitReturnStatement(child)
                    if stmt:
                        proc.body.append(stmt)

            self.current_procedure = None
            return proc
        except Exception as e:
            self.errors.append(f"Ошибка в процедуре: {e}")
            print(f"❌ Ошибка в процедуре: {e}")
            import traceback

            traceback.print_exc()
            return None

    def visitFunction(self, ctx):
        try:
            name = ctx.ID().getText()
            func = FunctionNode(name)

            self.current_function = func

            # Парсим параметры
            if ctx.parameterList():
                param_list = ctx.parameterList()
                for i in range(param_list.getChildCount()):
                    child = param_list.getChild(i)
                    if (
                        isinstance(child, TerminalNode)
                        and child.symbol.type == BSLParser.ID
                    ):
                        param = ParameterNode(child.getText(), False, False)
                        func.parameters.append(param)

            # Парсим тело функции
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if isinstance(child, BSLParser.ReturnStatementContext):
                    stmt = self.visitReturnStatement(child)
                    if stmt:
                        func.body.append(stmt)

            self.current_function = None
            return func
        except Exception as e:
            self.errors.append(f"Ошибка в функции: {e}")
            print(f"❌ Ошибка в функции: {e}")
            import traceback

            traceback.print_exc()
            return None

    def visitReturnStatement(self, ctx):
        try:
            stmt = ReturnStatementNode()
            if ctx.expression():
                stmt.expression = self.visit(ctx.expression())
            return stmt
        except Exception as e:
            self.errors.append(f"Ошибка в операторе Возврат: {e}")
            print(f"❌ Ошибка в операторе Возврат: {e}")
            import traceback

            traceback.print_exc()
            return None

    def visitExpression(self, ctx):
        try:
            return self.visitChildren(ctx)
        except Exception as e:
            self.errors.append(f"Ошибка в выражении: {e}")
            print(f"❌ Ошибка в выражении: {e}")
            import traceback

            traceback.print_exc()
            return None

    def visitPrimaryExpression(self, ctx):
        try:
            if ctx.ID():
                return VariableNode(ctx.ID().getText(), False)
            elif ctx.literal():
                return self.visit(ctx.literal())
            return None
        except Exception as e:
            self.errors.append(f"Ошибка в первичном выражении: {e}")
            print(f"❌ Ошибка в первичном выражении: {e}")
            import traceback

            traceback.print_exc()
            return None

    def visitLiteral(self, ctx):
        try:
            if ctx.STRING():
                return LiteralNode(ctx.getText(), "string")
            elif ctx.NUMBER():
                return LiteralNode(ctx.getText(), "number")
            elif ctx.getText() == "Истина":
                return LiteralNode(True, "boolean")
            elif ctx.getText() == "Ложь":
                return LiteralNode(False, "boolean")
            else:
                return LiteralNode(ctx.getText(), "unknown")
        except Exception as e:
            self.errors.append(f"Ошибка в литерале: {e}")
            print(f"❌ Ошибка в литерале: {e}")
            import traceback

            traceback.print_exc()
            return None

    def visit(self, ctx):
        if ctx is None:
            return None

        try:
            # Определяем тип контекста и вызываем соответствующий метод
            if isinstance(ctx, BSLParser.FileContext):  
                return self.visitFile(ctx)
            elif isinstance(ctx, BSLParser.ModuleDeclarationContext):
                return self.visitModuleDeclaration(ctx)
            elif isinstance(ctx, BSLParser.VariableDeclarationContext):
                return self.visitVariableDeclaration(ctx)
            elif isinstance(ctx, BSLParser.ProcedureContext):
                return self.visitProcedure(ctx)
            elif isinstance(ctx, BSLParser.FunctionContext):
                return self.visitFunction(ctx)
            elif isinstance(ctx, BSLParser.ReturnStatementContext):
                return self.visitReturnStatement(ctx)
            elif isinstance(ctx, BSLParser.ExpressionContext):
                return self.visitExpression(ctx)
            elif isinstance(ctx, BSLParser.PrimaryExpressionContext):
                return self.visitPrimaryExpression(ctx)
            elif isinstance(ctx, BSLParser.LiteralContext):
                return self.visitLiteral(ctx)

            return self.visitChildren(ctx)
        except Exception as e:
            self.errors.append(f"Ошибка при обходе узла {
                type(ctx).__name__}: {e}")
            return None

    def visitFile(self, ctx):
        # Проверка на пустой контекст
        if ctx is None:
            error_msg = "❌ Контекст файла пустой!"
            print(error_msg)
            self.errors.append(error_msg)
            return None

        # Создаём корневой модуль
        self.module = ModuleNode("module")

        try:
            # Обходим всех потомков
            child_count = 0
            print("🔍 Дочерние узлы файла:")
            for child in ctx.getChildren():
                child_count += 1
                child_type = type(child).__name__
                print(f"   {child_count}. {child_type}")

                if isinstance(child, BSLParser.ModuleDeclarationContext):
                    print("      → Это объявление модуля")
                    var = self.visitModuleDeclaration(child)
                    if var:
                        self.module.variables.append(var)
                elif isinstance(child, BSLParser.VariableDeclarationContext):
                    print("      → Это объявление переменной")
                    var = self.visitVariableDeclaration(child)
                    if var:
                        self.module.variables.append(var)
                elif isinstance(child, BSLParser.FunctionContext):
                    print("      → Это функция")
                    func = self.visitFunction(child)
                    if func:
                        self.module.functions.append(func)
                elif isinstance(child, BSLParser.ProcedureContext):
                    print("      → Это процедура")
                    proc = self.visitProcedure(child)
                    if proc:
                        self.module.procedures.append(proc)
                else:
                    print(f"      → Неизвестный тип: {child_type}")

            print(f"✅ Обработано {child_count} узлов")

            if self.module is None:
                error_msg = "❌ Модуль не создан!"
                print(error_msg)
                self.errors.append(error_msg)
                return None

            return self.module

        except Exception as e:
            error_msg = f"❌ Исключение при обходе: {e}"
            print(error_msg)
            self.errors.append(error_msg)
            import traceback
            traceback.print_exc()
            return None