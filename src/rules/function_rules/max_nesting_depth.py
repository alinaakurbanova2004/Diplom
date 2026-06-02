from typing import List
from src.parser.ast_nodes import ModuleNode, IfStatementNode, WhileLoopNode, ForLoopNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class MaxNestingDepth(BaseRule):
    """
    Правило FUN-06: Максимальная глубина вложенности
    Проверяет, что глубина вложенных условий и циклов не превышает 3.
    """

    def __init__(self):
        self.code = "FUN-06"
        self.name = "Слишком глубокое ветвление"
        self.description = "Глубина вложенности не должна превышать 3 уровня."
        self.severity = "WARNING"
        self.max_depth = 3

    def _check_nesting(self, node, current_depth, violations, module_name, context_name):
        """Рекурсивно проверяет глубину вложенности"""
        if current_depth > self.max_depth:
            line = node.range.start.line if node.range else 0
            violations.append(Violation(
                rule_code=self.code,
                rule_name=self.name,
                severity=self.severity,
                module_name=module_name,
                line=line,
                column=0,
                message=f"В {context_name} глубина вложенности {current_depth} превышает максимальную {self.max_depth}"
            ))
            return

        # Проверяем вложенные конструкции
        if isinstance(node, (IfStatementNode, WhileLoopNode, ForLoopNode)):
            if hasattr(node, 'body') and isinstance(node.body, list):
                for child in node.body:
                    self._check_nesting(child, current_depth + 1, violations, module_name, context_name)
            if isinstance(node, IfStatementNode):
                for branch in node.then_branch:
                    self._check_nesting(branch, current_depth + 1, violations, module_name, context_name)
                for branch in node.else_branch:
                    self._check_nesting(branch, current_depth + 1, violations, module_name, context_name)
        elif hasattr(node, 'body') and isinstance(node.body, list):
            for child in node.body:
                self._check_nesting(child, current_depth, violations, module_name, context_name)

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        for proc in module.procedures:
            for child in proc.body:
                self._check_nesting(child, 1, violations, module.name, f"процедуре '{proc.name}'")
        for func in module.functions:
            for child in func.body:
                self._check_nesting(child, 1, violations, module.name, f"функции '{func.name}'")
        return violations