from typing import List
from src.parser.ast_nodes import (FunctionNode,
                                  ModuleNode, ProcedureNode,  VariableNode)
from src.rules.base_rule import BaseRule
from src.visitor.base_visitor import ASTVisitor


class RuleCheckingVisitor(ASTVisitor):
    """Применяет все правила к AST и собирает нарушения"""

    def __init__(self, rules: List[BaseRule]):
        self.rules = rules
        self.violations = []
        self.current_module = None

    def visit_module(self, node: ModuleNode):
        self.current_module = node
        for rule in self.rules:  
            try:
                self.violations = rule.check(node)
                self.violations.extend(self.violations)
            except Exception as e:
                print(f"Ошибка в правиле {rule.code}: {e}")
        super().visit_module(node)
