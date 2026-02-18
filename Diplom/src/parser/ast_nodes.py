from dataclasses import dataclass
from typing import List
from enum import Enum

from Diplom.src.visitor.base_visitor import ASTVisitor


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

    def accept(self, visitor: ASTVisitor):
        """Принимает visitor и вызывает соответствующий метод"""
        pass


class ModuleNode(ASTNode):
    def __init__(self, name: str):
        super().__init__(NodeType.MODULE)
        self.name = name
        self.variables: List["VariableNode"] = []
        self.functions: List["FunctionNode"] = []
        self.procedures: List["ProcedureNode"] = []

    def accept(self, visitor: ASTVisitor):
        visitor.visit_module(self)


class FunctionNode(ASTNode):
    def __init__(self, name: str):
        super().__init__(NodeType.FUNCTION)
        self.name = name
        self.parameters: List["ParameterNode"] = []
        self.body: List[ASTNode] = []

    def accept(self, visitor: ASTVisitor):
        visitor.visit_function(self)


class ProcedureNode(ASTNode):
    def __init__(self, name: str):
        super().__init__(NodeType.PROCEDURE)
        self.name = name
        self.parameters: List["ParameterNode"] = []
        self.body: List[ASTNode] = []

    def accept(self, visitor: ASTVisitor):
        visitor.visit_procedure(self)


class ParameterNode(ASTNode):
    def __init__(
        self, name: str, by_value: bool = False,
        has_default_value: bool = False
    ):
        super().__init__(NodeType.PARAMETER)
        self.name = name
        self.by_value = by_value
        self.has_default_value = has_default_value
        
    def accept(self, visitor: ASTVisitor):
        visitor.visit_parameter(self)


class VariableNode(ASTNode):
    def __init__(self, name: str, is_export: bool = False):
        super().__init__(NodeType.VARIABLE)
        self.name = name
        self.is_export = is_export

    def accept(self, visitor: ASTVisitor):
        visitor.visit_variable(self)


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
        
    def accept(self, visitor: ASTVisitor):
        visitor.visit_binary_operation(self)


class LiteralNode(ExpressionNode):
    """Литерал (число, строка, булево значение)"""

    def __init__(self, value: any, literal_type: str):
        super().__init__(NodeType.LITERAL)
        self.value = value
        self.literal_type = literal_type
          
    def accept(self, visitor: ASTVisitor):
        visitor.visit_literal(self)


class IfStatementNode(ASTNode):
    """Оператор Если"""

    def __init__(self):
        super().__init__(NodeType.IF_STATEMENT)
        self.condition = None  # условие
        self.then_branch = []  # операторы в Тогда
        self.else_branch = []  # операторы в Иначе
        self.elif_branches = []  # список (условие, операторы) для ИначеЕсли
    
    def accept(self, visitor: ASTVisitor):
        visitor.visit_if_statement(self)


class WhileLoopNode(ASTNode):
    """Цикл Пока"""

    def __init__(self):
        super().__init__(NodeType.WHILE_LOOP)
        self.condition = None  # условие
        self.body = []  # тело цикла

    def accept(self, visitor: ASTVisitor):
        visitor.visit_while_loop(self)


class ReturnStatementNode(ASTNode):
    """Оператор Возврат"""

    def __init__(self):
        super().__init__(NodeType.RETURN_STATEMENT)
        self.expression = None  # выражение (может быть None)

    def accept(self, visitor: ASTVisitor):
        visitor.visit_return_statement(self)
