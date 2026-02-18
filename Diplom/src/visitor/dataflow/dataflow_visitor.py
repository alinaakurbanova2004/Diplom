from Diplom.src.parser.ast_nodes import VariableNode
from Diplom.src.visitor.base_visitor import ASTVisitor
from src.parser.ast_nodes import AssignmentNode


class DataFlowVisitor(ASTVisitor):
    """Анализирует поток данных (достигающие определения)"""

    def __init__(self):
        self.definitions = {}  # переменная -> строка определения
        self.uses = {}  # переменная -> список использований
        self.current_block = None

    def visit_assignment(self, node: AssignmentNode):
        # Запоминаем определение
        if hasattr(node.left, "name"):
            var_name = node.left.name
            self.definitions[var_name] = {
                "line": node.range.start.line if node.range else 0,
                "value": node.right,
                "block": self.current_block,
            }

        # Обходим правую часть (может содержать использования)
        if node.right:
            node.right.accept(self)

    def visit_variable(self, node: VariableNode):
        # Запоминаем использование
        if node.name not in self.uses:
            self.uses[node.name] = []

        self.uses[node.name].append(
            {
                "line": node.range.start.line if node.range else 0,
                "block": self.current_block,
            }
        )
