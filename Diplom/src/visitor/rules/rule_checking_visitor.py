from typing import List
from Diplom.src.parser.ast_nodes import (FunctionNode,
                                         ModuleNode,
                                         ProcedureNode,
                                         VariableNode)
from Diplom.src.rules.basic_rule import BaseRule
from Diplom.src.visitor.base_visitor import ASTVisitor


class RuleCheckingVisitor(ASTVisitor):
    """Применяет все правила к AST и собирает нарушения"""

    def __init__(self, rules: List[BaseRule]):
        self.rules = rules
        self.violations = []
        self.current_module = None

    def visit_module(self, node: ModuleNode):
        self.current_module = node
        # Применяем правила, которые проверяют весь модуль
        for rule in self.rules:
            if hasattr(rule, "check_module"):
                violations = rule.check_module(node)
                self.violations.extend(violations)

        super().visit_module(node)

    def visit_function(self, node: FunctionNode):
        # Применяем правила для функций
        for rule in self.rules:
            if hasattr(rule, "check_function"):
                violations = rule.check_function(node, self.current_module)
                self.violations.extend(violations)

        super().visit_function(node)

    def visit_procedure(self, node: ProcedureNode):
        # Применяем правила для процедур
        for rule in self.rules:
            if hasattr(rule, "check_procedure"):
                violations = rule.check_procedure(node, self.current_module)
                self.violations.extend(violations)

        super().visit_procedure(node)

    def visit_variable(self, node: VariableNode):
        # Применяем правила для переменных
        for rule in self.rules:
            if hasattr(rule, "check_variable"):
                violations = rule.check_variable(node, self.current_module)
                self.violations.extend(violations)

        super().visit_variable(node)
