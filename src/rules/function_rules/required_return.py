from typing import List
from src.parser.ast_nodes import ModuleNode, ReturnStatementNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class RequiredReturn(BaseRule):
    """
    Правило FUN-11: Функция должна возвращать значение
    Проверяет, что функция содержит оператор Возврат.
    """

    def __init__(self):
        self.code = "FUN-11"
        self.name = "Функция должна возвращать значение"
        self.description = "Функция должна содержать оператор 'Возврат'."
        self.severity = "ERROR"

    def _has_return(self, node) -> bool:
        """Проверяет, есть ли в теле узла оператор Возврат"""
        if isinstance(node, ReturnStatementNode):
            return True
        if hasattr(node, 'body') and isinstance(node.body, list):
            for child in node.body:
                if self._has_return(child):
                    return True
        return False

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        for func in module.functions:
            if not self._has_return(func):
                line = func.range.start.line if func.range else 0
                violations.append(Violation(
                    rule_code=self.code,
                    rule_name=self.name,
                    severity=self.severity,
                    module_name=module.name,
                    line=line,
                    column=0,
                    message=f"Функция '{func.name}' не содержит оператора 'Возврат'"
                ))
        return violations