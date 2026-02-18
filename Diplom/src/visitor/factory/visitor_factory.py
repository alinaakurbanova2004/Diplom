from typing import List
from src.visitor.base_visitor import ASTVisitor
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
from src.rules.base_rule import BaseRule


class VisitorFactory:
    """Фабрика для создания различных Visitor'ов"""

    @staticmethod
    def create_traversal_visitor():
        from src.visitor.traversal_visitor import TraversalVisitor

        return TraversalVisitor()

    @staticmethod
    def create_variable_collector():
        from src.visitor.collectors.variable_collector import VariableCollector

        return VariableCollector()

    @staticmethod
    def create_function_collector():
        from src.visitor.collectors.function_collector import FunctionCollector

        return FunctionCollector()

    @staticmethod
    def create_call_collector():
        from src.visitor.collectors.call_collector import CallCollector

        return CallCollector()

    @staticmethod
    def create_data_flow_visitor():
        from src.visitor.dataflow.dataflow_visitor import DataFlowVisitor

        return DataFlowVisitor()

    @staticmethod
    def create_rule_checking_visitor(rules: List[BaseRule]):
        from src.visitor.rules.rule_checking_visitor import RuleCheckingVisitor

        return RuleCheckingVisitor(rules)

    @staticmethod
    def create_composite_visitor(visitors: List[ASTVisitor]):
        """Создает составной Visitor, который запускает несколько за раз"""
        return CompositeVisitor(visitors)


class CompositeVisitor(ASTVisitor):
    """Запускает несколько Visitor'ов за один обход"""

    def __init__(self, visitors: List[ASTVisitor]):
        self.visitors = visitors

    def visit_module(self, node: ModuleNode):
        for visitor in self.visitors:
            if hasattr(visitor, "visit_module"):
                visitor.visit_module(node)

    def visit_function(self, node: FunctionNode):
        for visitor in self.visitors:
            if hasattr(visitor, "visit_function"):
                visitor.visit_function(node)

    def visit_procedure(self, node: ProcedureNode):
        for visitor in self.visitors:
            if hasattr(visitor, "visit_procedure"):
                visitor.visit_procedure(node)

    def visit_variable(self, node: VariableNode):
        for visitor in self.visitors:
            if hasattr(visitor, "visit_variable"):
                visitor.visit_variable(node)

    def visit_parameter(self, node: ParameterNode):
        for visitor in self.visitors:
            if hasattr(visitor, "visit_parameter"):
                visitor.visit_parameter(node)

    def visit_if_statement(self, node: IfStatementNode):
        for visitor in self.visitors:
            if hasattr(visitor, "visit_if_statement"):
                visitor.visit_if_statement(node)

    def visit_while_loop(self, node: WhileLoopNode):
        for visitor in self.visitors:
            if hasattr(visitor, "visit_while_loop"):
                visitor.visit_while_loop(node)

    def visit_return_statement(self, node: ReturnStatementNode):
        for visitor in self.visitors:
            if hasattr(visitor, "visit_return_statement"):
                visitor.visit_return_statement(node)

    def visit_binary_operation(self, node: BinaryOperationNode):
        for visitor in self.visitors:
            if hasattr(visitor, "visit_binary_operation"):
                visitor.visit_binary_operation(node)

    def visit_literal(self, node: LiteralNode):
        for visitor in self.visitors:
            if hasattr(visitor, "visit_literal"):
                visitor.visit_literal(node)
