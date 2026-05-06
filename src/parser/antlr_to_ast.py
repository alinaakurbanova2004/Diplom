from .antlr.BSLVisitor import BSLVisitor
from .antlr.BSLParser import BSLParser
from antlr4.tree.Tree import TerminalNode
from src.parser.ast_nodes import AssignmentNode, Position, Range
from src.parser.ast_nodes import (
    ModuleNode,
    FunctionNode,
    ProcedureNode,
    VariableNode,
    ParameterNode,
    ReturnStatementNode,
    LiteralNode,
    ForLoopNode,
    WhileLoopNode,
)


class AntlrToAST(BSLVisitor):
    """Преобразует ANTLR AST в AST"""

    def __init__(self):
        self.module = None
        self.current_function = None
        self.current_procedure = None
        self.errors = []

        # Поля для сбора переменных
        self.seen_vars = {}  # словарь:
        # имя переменной -> список мест использования
        self.current_scope = []  # стек текущих областей видимости

    def visitVariableDeclaration(self, ctx):
        try:
            name = ctx.ID().getText()
            print(f"🔍 Найдена переменная: {name}")
            node_range = self._get_id_range(ctx)
            is_export = (
                ctx.getChildCount() > 2 and ctx.getChild(2).getText() == "Экспорт"
            )

            var_node = VariableNode(name, is_export, node_range)
            return var_node

        except Exception as e:
            self.errors.append(f"Ошибка в переменной: {e}")
            print(f"❌ Ошибка в объявлении переменной: {e}")
            import traceback

            traceback.print_exc()
            return None

    def visitLocalVariableDeclaration(self, ctx):
        try:
            # Получаем имя переменной (первый ID)
            name = None
            id_token = None
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if (
                    isinstance(child, TerminalNode)
                    and child.symbol.type == BSLParser.ID
                ):
                    name = child.getText()
                    id_token = child
                    break

            if name is None:
                return None
            

            node_range = self._get_id_range(id_token) 
    
            var_node = VariableNode(name, False, node_range)
            
            return var_node

        except Exception as e:
            self.errors.append(f"Ошибка в объявлении локальной переменной: {e}")
            print(f"❌ Ошибка в локальной переменной: {e}")
            return None
        
    def _get_id_range(self, id_node) -> Range:
        """Получает range для ID токена"""
        if id_node is None:
            return None
    
        # Если передан контекст с методом ID()
        if hasattr(id_node, 'ID'):
            id_token = id_node.ID().symbol
            name = id_node.ID().getText()
        # Если передан сам TerminalNode
        elif isinstance(id_node, TerminalNode) and id_node.symbol.type == BSLParser.ID:
            id_token = id_node.symbol
            name = id_node.getText()
        else:
            return None
    
        return Range(
            start=Position(line=id_token.line, column=id_token.column + 1),
            end=Position(line=id_token.line, column=id_token.column + len(name) + 1)
        )

    def _process_statement(self, stmt_ctx, container):
        # Перебираем все дочерние элементы statement'а
        for j in range(stmt_ctx.getChildCount()):
            inner_child = stmt_ctx.getChild(j)

            # Если это присваивание
            if isinstance(inner_child, BSLParser.AssignmentContext):
                self.visitAssignment(inner_child)
                print("Найдено присваивание")

            # Если это цикл Для
            elif isinstance(inner_child, BSLParser.ForStatementContext):
                print("Найден цикл Для")
                # Обрабатываем тело цикла
                for k in range(inner_child.getChildCount()):
                    loop_child = inner_child.getChild(k)
                    if isinstance(loop_child, BSLParser.StatementContext):
                        self._process_statement(loop_child, container)

            # Если это цикл Пока
            elif isinstance(inner_child, BSLParser.WhileStatementContext):
                print("Найден цикл Пока")
                for k in range(inner_child.getChildCount()):
                    loop_child = inner_child.getChild(k)
                    if isinstance(loop_child, BSLParser.StatementContext):
                        self._process_statement(loop_child, container)

            # Если это условие
            elif isinstance(inner_child, BSLParser.IfStatementContext):
                print("Найдено условие")
                # Обрабатываем все statement'ы внутри условия
                for k in range(inner_child.getChildCount()):
                    if_child = inner_child.getChild(k)
                    if isinstance(if_child, BSLParser.StatementContext):
                        self._process_statement(if_child, container)

            # Если это локальная переменная
            elif isinstance(inner_child, BSLParser.LocalVariableDeclarationContext):
                var_node = self.visitLocalVariableDeclaration(inner_child)
                if var_node:
                    container.local_vars.append(var_node)
                    container.body.append(var_node)
                    print(f"✅ Добавлена локальная переменная: {var_node.name}")

            # Если это return statement
            elif isinstance(inner_child, BSLParser.ReturnStatementContext):
                stmt = self.visitReturnStatement(inner_child)
                if stmt:
                    container.body.append(stmt)

                # Рекурсивно обрабатываем вложенные statement'ы
            elif isinstance(inner_child, BSLParser.StatementContext):
                self._process_statement(inner_child, container)
            elif isinstance(inner_child, BSLParser.ExpressionContext):
                self._process_expression(inner_child, container)

    def visitProcedure(self, ctx):
        try:
            name = ctx.ID().getText()
            node_range = self._get_id_range(ctx)
            proc = ProcedureNode(name,node_range)
            self.current_procedure = proc
            self.current_scope.append(f"procedure:{name}")
            # Парсим параметры
            if ctx.parameterList():
                param_list = ctx.parameterList()
                print(
                    f"   📊 Список параметров процедуры {name}: {param_list.getChildCount()} детей"
                )

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
                            print(
                                f" ✅ Добавлен параметр: {param_node.name}"
                            )

                    # Запасной вариант: если это прямой ID,
                    # если нет ParameterContext
                    elif (
                        isinstance(child, TerminalNode)
                        and child.symbol.type == BSLParser.ID
                    ):
                        param = ParameterNode(child.getText(), False, False)
                        proc.parameters.append(param)
                        print(f"         ⚠️ Прямой ID параметр: {param.name}")

            print(f"   ✅ Всего параметров: {len(proc.parameters)}")

            # Парсим тело процедуры
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                # Проверяем, является ли ребенок statement'ом
                if isinstance(child, BSLParser.StatementContext):
                    # Обрабатываем statement
                    self._process_statement(child, proc)

            self.current_scope.pop()
            self.current_procedure = None
            return proc

        except Exception as e:
            self.errors.append(f"Ошибка в процедуре: {e}")
            print(f"❌ Ошибка в процедуре: {e}")
            import traceback

            traceback.print_exc()
            return None

    def visitVariable(self, ctx):
        """
        Обрабатывает использование переменной и собирает информацию о ней
        """
        try:
               # Получаем range только для ID
            node_range = self._get_id_range(ctx)
            if node_range is None:
                # Fallback: пробуем получить имя другим способом
                var_name = ctx.getText()
                node_range = self._get_range(ctx)
            else:
                var_name = ctx.ID().getText() if hasattr(ctx, 'ID') else ctx.getText()
        
            print(f"DEBUG: переменная {var_name} at line={node_range.start.line}, col={node_range.start.column}")
            # Определяем контекст
            current_context = None
            if self.current_function:
                current_context = self.current_function
            elif self.current_procedure:
                current_context = self.current_procedure

            # Получаем текущую область видимости
            if self.current_scope:
                scope = "/".join(self.current_scope)
            else:
                scope = "global"

            # Запоминаем это использование переменной
            if var_name not in self.seen_vars:
                self.seen_vars[var_name] = []

            self.seen_vars[var_name].append(
                {
                    "scope": scope,
                    "line": ctx.start.line if hasattr(ctx, "start") else 0,
                    "context": current_context,
                }
            )

            # Если мы внутри функции/процедуры
            if current_context:
                # Проверяем, не является ли эта переменная параметром
                is_parameter = False
                for param in current_context.parameters:
                    if param.name == var_name:
                        is_parameter = True
                        break

                # Если не параметр и мы её ещё не добавляли как локальную
                if not is_parameter:
                    # Проверяем, есть ли уже такая переменная в local_vars
                    exists = False
                    for var in current_context.local_vars:
                        if var.name == var_name:
                            exists = True
                            break

                    if not exists:
                        # Добавляем как локальную переменную
                        var_node = VariableNode(var_name, False, node_range)
                        current_context.local_vars.append(var_node)
                        indent = (
                            "         "
                            if self.current_function or self.current_procedure
                            else ""
                        )
                        print(
                            f"{
                                indent} Найдена локальная переменная: {var_name} (в {scope})"
                        )

            return VariableNode(var_name, False,node_range)

        except Exception as e:
            self.errors.append(f"Ошибка при обработке переменной: {e}")
            return None
        
    def _get_range(self, ctx) -> Range:
        """Безопасное получение диапазона из контекста ANTLR"""
        if ctx is None:
            print("DEBUG _get_range: ctx is None")
            return None
    
        if hasattr(ctx, 'start') and hasattr(ctx, 'stop'):
            if ctx.start is not None and ctx.stop is not None:
                start_column = ctx.start.column +1
                end_column = ctx.stop.column + 1
                print(f"DEBUG _get_range: start.line={ctx.start.line}, stop.line={ctx.stop.line}")
                return Range(
                    start=Position(line=ctx.start.line, column=start_column),
                    end=Position(line=ctx.stop.line, column=end_column)
                )
            else:
                print(f"DEBUG _get_range: start или stop = None для {type(ctx).__name__}")
                return None
    
        print(f"DEBUG _get_range: нет start/stop для {type(ctx).__name__}")
        return None
    
    def visitFunction(self, ctx):
        try:
            name = ctx.ID().getText()
            print(f"🔍 Найдена функция: {name}")
            node_range = self._get_range(ctx)
            func = FunctionNode(name, node_range)

            self.current_function = func
            self.current_scope.append(f"function:{name}")
            # Парсим параметры
            if ctx.parameterList():
                param_list = ctx.parameterList()
                print(
                    f"   📊 Список параметров функции {name}: {param_list.getChildCount()} детей"
                )

                # Перебираем все дочерние элементы
                for i in range(param_list.getChildCount()):
                    child = param_list.getChild(i)
                    child_type = type(child).__name__
                    print(f"      Ребенок {i}: {child_type}")

                    # Если это контекст параметра
                    if isinstance(child, BSLParser.ParameterContext):
                        param_node = self.visitParameter(child)
                        if param_node:
                            func.parameters.append(param_node)
                            print(f" ✅ Добавлен параметр: {param_node.name}")

                    # Запасной вариант: если это прямой ID
                    # если нет, ParameterContext
                    elif (
                        isinstance(child, TerminalNode)
                        and child.symbol.type == BSLParser.ID
                    ):
                        param = ParameterNode(child.getText(), False, False)
                        func.parameters.append(param)
                        print(f"⚠️ Прямой ID параметр: {param.name}")

            print(
                f" ✅ Всего параметров в функции {name}: {len(func.parameters)}"
            )

            # Парсим тело функции
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)

                if isinstance(child, BSLParser.StatementContext):
                    self._process_statement(child, func)
            self.current_scope.pop()
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
            id_token = None
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if (
                    isinstance(child, TerminalNode)
                    and child.symbol.type == BSLParser.ID
                ):
                    name = child.getText()
                    id_token = child
                    break

            # Получаем range для параметра
            node_range = self._get_id_range(id_token)

            # Проверяем, есть ли ключевое слово Знач
            by_value = False
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if isinstance(child, TerminalNode) and child.getText() == "Знач":
                    by_value = True
                    break

            # Проверяем, есть ли значение по умолчанию
            has_default = ctx.getChildCount() > 2 and ctx.getChild(2).getText() == "="

            print(
                f"      → Параметр: {name}, Знач: {by_value}, умолчание: {has_default}"
            )

            return ParameterNode(name, by_value, has_default, node_range)
        except Exception as e:
            self.errors.append(f"Ошибка в параметре: {e}")
            return None

    def visitReturnStatement(self, ctx):
        try:
            node_range = self._get_range(ctx)
            stmt = ReturnStatementNode(node_range)
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
                return self.visitVariable(ctx)
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
            node_range = self._get_range(ctx)
            if ctx.STRING():
                return LiteralNode(ctx.getText(), "string", node_range)
            elif ctx.NUMBER():
                return LiteralNode(ctx.getText(), "number", node_range)
            elif ctx.getText() == "Истина":
                return LiteralNode(True, "boolean", node_range)
            elif ctx.getText() == "Ложь":
                return LiteralNode(False, "boolean", node_range)
            else:
                return LiteralNode(ctx.getText(), "unknown", node_range)
        except Exception as e:
            self.errors.append(f"Ошибка в литерале: {e}")
            print(f"❌ Ошибка в литерале: {e}")
            import traceback

            traceback.print_exc()
            return None

    def visitForStatement(self, ctx):

        try:
            print("🔍 Найден цикл Для")
            node_range = self._get_range(ctx)
            # Создаём узел цикла
            for_node = ForLoopNode(node_range)

            # Получаем переменную-счётчик (первый ID после FOR)
            counter_var = None
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if (
                    isinstance(child, TerminalNode)
                    and child.symbol.type == BSLParser.ID
                ):
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
            node_range = self._get_range(ctx)
            # Создаём узел цикла
            while_node = WhileLoopNode(node_range)

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
            if isinstance(ctx, BSLParser.BslFileContext):
                return self.visitFile(ctx)
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
            elif isinstance(ctx, BSLParser.AssignmentContext):
                return self.visitAssignment(ctx)

            return self.visitChildren(ctx)
        except Exception as e:
            self.errors.append(
                f"Ошибка при обходе узла {type(ctx).__name__}: {e}"
            )
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

                if isinstance(child, BSLParser.VariableDeclarationContext):
                    print("      → Это объявление глобальной переменной")
                    var = self.visitVariableDeclaration(child)
                    if var:
                        self.module.variables.append(var)
                elif isinstance(child, 
                                BSLParser.LocalVariableDeclarationContext):
                    print("      → Это объявление локальной переменной")
                    var = self.visitLocalVariableDeclaration(child)
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

    def _process_expression(self, expr_ctx, container):
        """Рекурсивно обходит выражение в поисках переменных"""

        for i in range(expr_ctx.getChildCount()):
            child = expr_ctx.getChild(i)

            if isinstance(child, BSLParser.PrimaryExpressionContext):
                self._process_primary_expression(child, container)
            elif isinstance(child, BSLParser.ExpressionContext):
                self._process_expression(child, container)

    def _process_primary_expression(self, prim_ctx, container):
        """Обрабатывает первичное выражение"""

        for i in range(prim_ctx.getChildCount()):
            child = prim_ctx.getChild(i)

            if isinstance(child, TerminalNode) and child.symbol.type == BSLParser.ID:
                self.visitVariable(child)

    def visitAssignment(self, ctx):
        """Обрабатывает оператор присваивания"""
        try:
            node_range = self._get_range(ctx)
            left_node = None
            right_node = None
        
            # Находим переменную слева от '='
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
            
                if (isinstance(child, TerminalNode) and child.symbol.type == BSLParser.ID):
                    var_name = child.getText()
                    # Регистрируем переменную (это добавит её в local_vars)
                    left_node = self.visitVariable(child)
                    print(f"      📝 Присваивание переменной: {var_name}")
                    break
        
            # Обрабатываем правую часть
            for i in range(ctx.getChildCount()):
                child = ctx.getChild(i)
                if isinstance(child, BSLParser.ExpressionContext):
                    right_node = self.visit(child)
                    break
        
            if left_node and right_node:
                assign_node = AssignmentNode(left_node, right_node, node_range)
            
                if self.current_procedure:
                    self.current_procedure.body.append(assign_node)
                    print(" Добавлен узел присваивания в процедуру")
                elif self.current_function:
                    self.current_function.body.append(assign_node)
                    print("Добавлен узел присваивания в функцию")
                return assign_node
        
            return None
    
        except Exception as e:
            self.errors.append(f"Ошибка в присваивании: {e}")
            return None