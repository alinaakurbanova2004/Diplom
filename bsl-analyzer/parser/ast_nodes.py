from dataclasses import dataclass


@dataclass
class Position:
    line: int
    column: int


@dataclass
class Range:
    start: Position
    end: Position


class ASTNode:
    """Базовый класс для всех узлов"""

    def __init__(self, node_type: str, range: Range = None):
        self.node_type = node_type
        self.range = range


class ModuleNode(ASTNode):
    """Корневой узел модуля"""

    def __init__(self, name: str):
        super().__init__("module")
        self.name = name
        self.functions = []
        self.procedures = []
        self.variables = []


class FunctionNode(ASTNode):
    """Узел функции"""

    def __init__(self, name: str):
        super().__init__("function")
        self.name = name
        self.parameters = []
