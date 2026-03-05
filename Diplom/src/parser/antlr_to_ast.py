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
    ForLoopNode,
    WhileLoopNode
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
    
    def visitLocalVariableDeclaration(self, ctx):
        try:
            name = ctx.ID().getText()
            print(f"🔍 Найдена локальная переменная: {name}")
        
            is_export = (
                ctx.getChildCount() > 2 and
                ctx.getChild(2).getText() == "Экспорт"
            )
        
            var_node = VariableNode(name, is_export)
        
            # Добавляем к текущей функции или процедуре
            if self.current_function:
                self.current_function.local_vars.append(var_node)
            elif self.current_procedure:
                self.current_procedure.local_vars.append(var_node)
        
            return var_node
        except Exception as e:
            self.errors.append(f"Ошибка в локальной переменной: {e}")
            return None
    
    def visitProcedure(self, ctx):
        try:
            name = ctx.ID().getText()
            proc = ProcedureNode(name)

            self.current_procedure = proc

            # Парсим параметры 
            if ctx.parameterList():
                param_list = ctx.parameterList()
                print(f"   📊 Список параметров процедуры {
                    name}: {param_list.getChildCount()} детей")
            
                # Перебираем все дочерние элементы
                for i in range(param_list.getChildCount()):
                    child = param_list.getChild(i)
                    child_type = type(child).__name__
                    print(f"      Ребенок {i}: {child_type}")
                
                    # Если это контекст параметра
                    if isinstance(child, BSLParser.ParameterContext):
                        param_node = self.visitParameter(child)
                        if param_node:
                            proc.parameters.append(param_node)
                            print(f"         ✅ Добавлен параметр: {
                                param_node.name}")
                
                    # Запасной вариант: если это прямой ID,
                    # если нет ParameterContext
                    elif isinstance(child, TerminalNode) and \
                            child.symbol.type == BSLParser.ID:
                        param = ParameterNode(child.getText(), False, False)
                        proc.parameters.append(param)
                        print(f"         ⚠️ Прямой ID параметр: {param.name}")
        
            print(f"   ✅ Всего параметров: {len(proc.parameters)}")

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
            print(f"🔍 Найдена функция: {name}")
            func = FunctionNode(name)

            self.current_function = func

            # Парсим параметры
            if ctx.parameterList():
                param_list = ctx.parameterList()
                print(f"   📊 Список параметров функции {
                    name}: {param_list.getChildCount()} детей")
            
                # Перебираем все дочерние элементы
                for i in range(param_list.getChildCount()):
                    child = param_list.getChild(i)
                    child_type = type(child).__name__
                    print(f"      Ребенок {i}: {child_type}")
                
                    # Если это контекст параметра
                    if isinstance(child, BSLParser.ParameterContext):
                        param_node = self.visitParameter(child)
                        if param_node:
                            func.parameters.append(
                                param_node)
                            print(f" ✅ Добавлен параметр: {param_node.name}")
                
                    # Запасной вариант: если это прямой ID
                    # если нет, ParameterContext
                    elif isinstance(child, TerminalNode) and \
                            child.symbol.type == BSLParser.ID:
                        param = ParameterNode(child.getText(), False, False)
                        func.parameters.append(param)
                        print(f"⚠️ Прямой ID параметр: {param.name}")
        
            print(f"   ✅ Всего параметров в функции {name}: {
                len(func.parameters)}")

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
        
    def visitParameter(self, ctx):
        """Обрабатывает параметр функции/процедуры"""
        try:
            # Получаем имя параметра (первый ID)
            name = None
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if isinstance(child, TerminalNode) and \
                   child.symbol.type == BSLParser.ID:
                    name = child.getText()
                    break
        
            # Проверяем, есть ли ключевое слово Знач
            by_value = False
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if isinstance(child, TerminalNode) and \
                        child.getText() == "Знач":
                    by_value = True
                    break
        
            # Проверяем, есть ли значение по умолчанию
            has_default = ctx.getChildCount() > 2 and \
                ctx.getChild(2).getText() == "="
        
            print(f"      → Параметр: {
                name}, Знач: {by_value}, умолчание: {has_default}")
        
            return ParameterNode(name, by_value, has_default)
        except Exception as e:
            self.errors.append(f"Ошибка в параметре: {e}")
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
        
    def visitForStatement(self, ctx):
  
        try:
            print("🔍 Найден цикл Для")
        
            # Создаём узел цикла 
            for_node = ForLoopNode()
        
            # Получаем переменную-счётчик (первый ID после FOR)
            counter_var = None
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if isinstance(child,
                              TerminalNode
                              ) and child.symbol.type == BSLParser.ID:
                    counter_var = child.getText()
                    print(f"      Счётчик: {counter_var}")
                    break
        
            # Получаем начальное значение (первое выражение)
            start_expr = None
            if ctx.expression(0):
                start_expr = self.visit(ctx.expression(0))
                print(f"      Начало: {start_expr}")
        
            # Получаем конечное значение (второе выражение)
            end_expr = None
            if ctx.expression(1):
                end_expr = self.visit(ctx.expression(1))
                print(f"      Конец: {end_expr}")
        
            # Собираем операторы тела цикла
            body_statements = []
            for child in ctx.getChildren():
                if isinstance(child, BSLParser.StatementContext):
                    stmt = self.visit(child)
                    if stmt:
                        body_statements.append(stmt)
        
            print(f"      Операторов в теле: {len(body_statements)}")
        
            # Здесь нужно вернуть созданный узел
            for_node.counter = counter_var
            for_node.start = start_expr
            for_node.end = end_expr
            for_node.body = body_statements
            return for_node
        
        except Exception as e:
            self.errors.append(f"Ошибка в цикле Для: {e}")
            print(f"❌ Ошибка в цикле Для: {e}")
            import traceback
            traceback.print_exc()
            return None

    def visitWhileStatement(self, ctx):
        """
        Обрабатывает цикл Пока
        """
        try:
            print("🔍 Найден цикл Пока")
        
            # Создаём узел цикла 
            while_node = WhileLoopNode()
        
            # Получаем условие цикла
            if ctx.expression():
                while_node.condition = self.visit(ctx.expression())
                print(f"      Условие: {while_node.condition}")
        
            # Собираем операторы тела цикла
            body_statements = []
            for child in ctx.getChildren():
                if isinstance(child, BSLParser.StatementContext):
                    stmt = self.visit(child)
                    if stmt:
                        body_statements.append(stmt)
        
            while_node.body = body_statements
            print(f"      Операторов в теле: {len(body_statements)}")
        
            return while_node
        
        except Exception as e:
            self.errors.append(f"Ошибка в цикле Пока: {e}")
            print(f"❌ Ошибка в цикле Пока: {e}")
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
            elif isinstance(ctx, BSLParser.ForStatementContext):
                return self.visitForStatement(ctx)
            elif isinstance(ctx, BSLParser.WhileStatementContext):
                return self.visitWhileStatement(ctx)
            elif isinstance(ctx, BSLParser.ParameterContext):
                return self.visitParameter(ctx)
            elif isinstance(ctx, BSLParser.LocalVariableDeclarationContext):
                return self.visitLocalVariableDeclaration(ctx)

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