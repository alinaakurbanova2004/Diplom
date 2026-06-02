from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class MissingComments(BaseRule):
    """
    Правило FUN-07: Недостаточно комментариев
    Проверяет, что доля комментариев в коде не менее заданного процента.
    """

    def __init__(self):
        self.code = "FUN-07"
        self.name = "Недостаточно комментариев"
        self.description = "Код должен содержать достаточное количество комментариев."
        self.severity = "INFO"
        self.min_comment_ratio = 5  # минимум 5% строк должны быть комментариями

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if hasattr(module, 'original_code') and module.original_code:
            lines = module.original_code.split('\n')
            total_lines = len([l for l in lines if l.strip()])
            comment_lines = len([l for l in lines if l.strip().startswith('//')])
            ratio = comment_lines / total_lines * 100 if total_lines > 0 else 0

            if ratio < self.min_comment_ratio and total_lines > 20:
                violations.append(Violation(
                    rule_code=self.code,
                    rule_name=self.name,
                    severity=self.severity,
                    module_name=module.name,
                    line=1,
                    column=1,
                    message=f"Доля комментариев {ratio:.1f}% (мин. {self.min_comment_ratio}%)"
                ))
        return violations