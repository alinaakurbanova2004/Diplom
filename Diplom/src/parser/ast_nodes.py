from dataclasses import dataclass
from typing import List
from enum import Enum


class NodeType(Enum):
    MODULE = "module"
    FUNCTION = "function"
    PROCEDURE = "procedure"
    VARIABLE = "variable"
    ASSIGNMENT = "assignment"
    IF_STATEMENT = "if_statement"
    WHILE_LOOP = "while_loop"
    FOR_LOOP = "for_loop"
    RETURN_STATEMENT = "return_statement"
    EXPRESSION = "expression"
    BINARY_OPERATION = "binary_operation"
    FUNCTION_CALL = "function_call"
    LITERAL = "literal"
    PARAMETER = "parameter"


@dataclass
class Position:
    line: int
    column: int


@dataclass
class Range:
    start: Position
    end: Position


class ASTNode:
    def __init__(self, node_type: NodeType, range: Range = None):
        self.node_type = node_type
        self.range = range


class ModuleNode(ASTNode):
    def __init__(self, name: str):
        super().__init__(NodeType.MODULE)
        self.name = name
        self.variables: List["VariableNode"] = []
        self.functions: List["FunctionNode"] = []
        self.procedures: List["ProcedureNode"] = []


class FunctionNode(ASTNode):
    def __init__(self, name: str):
        super().__init__(NodeType.FUNCTION)
        self.name = name
        self.parameters: List["ParameterNode"] = []
        self.body: List[ASTNode] = []


class ProcedureNode(ASTNode):
    def __init__(self, name: str):
        super().__init__(NodeType.PROCEDURE)
        self.name = name
        self.parameters: List["ParameterNode"] = []
        self.body: List[ASTNode] = []


class ParameterNode(ASTNode):
    def __init__(self, name: str, by_value: bool = False):
        super().__init__(NodeType.PARAMETER)
        self.name = name
        self.by_value = by_value


class VariableNode(ASTNode):
    def __init__(self, name: str, is_export: bool = False):
        super().__init__(NodeType.VARIABLE)
        self.name = name
        self.is_export = is_export


class ExpressionNode(ASTNode):
    """Базовый класс для выражений"""

    def __init__(self, node_type: NodeType):
        super().__init__(node_type)


class BinaryOperationNode(ExpressionNode):
    """Бинарная операция (a + b, a > b, и т.д.)"""

    def __init__(self, operator: str, left: ASTNode, right: ASTNode):
        super().__init__(NodeType.BINARY_OPERATION)
        self.operator = operator
        self.left = left
        self.right = right


class LiteralNode(ExpressionNode):
    """Литерал (число, строка, булево значение)"""

    def __init__(self, value: any, literal_type: str):
        super().__init__(NodeType.LITERAL)
        self.value = value
        self.literal_type = literal_type  # 'number', 'string', 'boolean'


class IfStatementNode(ASTNode):
    """Оператор Если"""

    def __init__(self):
        super().__init__(NodeType.IF_STATEMENT)
        self.condition = None  # условие
        self.then_branch = []  # операторы в Тогда
        self.else_branch = []  # операторы в Иначе
        self.elif_branches = []  # список (условие, операторы) для ИначеЕсли


class WhileLoopNode(ASTNode):
    """Цикл Пока"""

    def __init__(self):
        super().__init__(NodeType.WHILE_LOOP)
        self.condition = None  # условие
        self.body = []  # тело цикла


class ReturnStatementNode(ASTNode):
    """Оператор Возврат"""

    def __init__(self):
        super().__init__(NodeType.RETURN_STATEMENT)
        self.expression = None  # выражение (может быть None)
