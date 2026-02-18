from Diplom.src.parser.ast_nodes import (
    BinaryOperationNode,
    FunctionNode,
    IfStatementNode,
    LiteralNode,
    ModuleNode,
    ProcedureNode,
    ReturnStatementNode,
    VariableNode,
    WhileLoopNode,
)


class ASTVisitor:
    """Базовый класс Visitor для обхода AST"""

    def visit_module(self, node: ModuleNode):
        pass

    def visit_function(self, node: FunctionNode):
        pass

    def visit_procedure(self, node: ProcedureNode):
        pass

    def visit_variable(self, node: VariableNode):
        pass

    def visit_if_statement(self, node: IfStatementNode):
        pass

    def visit_while_loop(self, node: WhileLoopNode):
        pass

    def visit_return_statement(self, node: ReturnStatementNode):
        pass

    def visit_binary_operation(self, node: BinaryOperationNode):
        pass

    def visit_literal(self, node: LiteralNode):
        pass
