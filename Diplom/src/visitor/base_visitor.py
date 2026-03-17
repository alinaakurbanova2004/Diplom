from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from src.parser.ast_nodes import (
        ModuleNode,
        FunctionNode,
        ProcedureNode,
        VariableNode,
        IfStatementNode,
        WhileLoopNode,
        ReturnStatementNode,
        BinaryOperationNode,
        LiteralNode,
        ParameterNode,
    )


class ASTVisitor:
    """Базовый класс Visitor для обхода AST"""

    def visit_module(self, node: "ModuleNode"):
        pass

    def visit_function(self, node: "FunctionNode"):
        pass

    def visit_procedure(self, node: "ProcedureNode"):
        pass

    def visit_variable(self, node: "VariableNode"):
        pass

    def visit_parameter(self, node: "ParameterNode"):
        pass

    def visit_if_statement(self, node: "IfStatementNode"):
        pass

    def visit_while_loop(self, node: "WhileLoopNode"):
        pass

    def visit_return_statement(self, node: "ReturnStatementNode"):
        pass

    def visit_binary_operation(self, node: "BinaryOperationNode"):
        pass

    def visit_literal(self, node: "LiteralNode"):
        pass
