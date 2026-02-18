from Diplom.src.parser.ast_nodes import (FunctionNode,
                                         ModuleNode,
                                         ProcedureNode,
                                         VariableNode)
from Diplom.src.visitor.base_visitor import ASTVisitor


class VariableCollector(ASTVisitor):
    """Собирает все переменные в модуле"""

    def __init__(self):
        self.variables = []
        self.current_scope = []

    def visit_module(self, node: ModuleNode):
        self.current_scope.append("module")
        super().visit_module(node)
        self.current_scope.pop()

    def visit_function(self, node: FunctionNode):
        self.current_scope.append(f"function:{node.name}")
        # Собираем параметры
        for param in node.parameters:
            self.variables.append(
                {
                    "name": param.name,
                    "scope": ".".join(self.current_scope),
                    "type": "parameter",
                    "line": param.range.start.line if param.range else 0,
                }
            )
        super().visit_function(node)
        self.current_scope.pop()

    def visit_procedure(self, node: ProcedureNode):
        self.current_scope.append(f"procedure:{node.name}")
        # Собираем параметры
        for param in node.parameters:
            self.variables.append(
                {
                    "name": param.name,
                    "scope": ".".join(self.current_scope),
                    "type": "parameter",
                    "line": param.range.start.line if param.range else 0,
                }
            )
        super().visit_procedure(node)
        self.current_scope.pop()

    def visit_variable(self, node: VariableNode):
        # Собираем использование переменных
        self.variables.append(
            {
                "name": node.name,
                "scope": ".".join(self.current_scope),
                "type": "usage",
                "line": node.range.start.line if node.range else 0,
                "is_export": node.is_export,
            }
        )
