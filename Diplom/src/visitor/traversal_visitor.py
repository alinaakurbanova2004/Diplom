from Diplom.src.parser.ast_nodes import (
    FunctionNode,
    IfStatementNode,
    ModuleNode,
    ProcedureNode, WhileLoopNode)
from Diplom.src.visitor.base_visitor import ASTVisitor


class TraversalVisitor(ASTVisitor):
    """Выполняет обход AST и вызывает соответствующие методы"""

    def visit_module(self, node: ModuleNode):
        # Обходим переменные
        for var in node.variables:
            var.accept(self)

        # Обходим функции
        for func in node.functions:
            func.accept(self)

        # Обходим процедуры
        for proc in node.procedures:
            proc.accept(self)

    def visit_function(self, node: FunctionNode):
        # Обходим параметры
        for param in node.parameters:
            param.accept(self)

        # Обходим тело функции
        for stmt in node.body:
            stmt.accept(self)

    def visit_procedure(self, node: ProcedureNode):
        # Обходим параметры
        for param in node.parameters:
            param.accept(self)

        # Обходим тело процедуры
        for stmt in node.body:
            stmt.accept(self)

    def visit_if_statement(self, node: IfStatementNode):
        # Обходим условие
        if node.condition:
            node.condition.accept(self)

        # Обходим ветку Тогда
        for stmt in node.then_branch:
            stmt.accept(self)

        # Обходим ветки ИначеЕсли
        for condition, statements in node.elif_branches:
            condition.accept(self)
            for stmt in statements:
                stmt.accept(self)

        # Обходим ветку Иначе
        for stmt in node.else_branch:
            stmt.accept(self)

    def visit_while_loop(self, node: WhileLoopNode):
        # Обходим условие
        if node.condition:
            node.condition.accept(self)

        # Обходим тело цикла
        for stmt in node.body:
            stmt.accept(self)
