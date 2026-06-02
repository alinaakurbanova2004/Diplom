from typing import List
import re
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class MaxJoinsInQuery(BaseRule):
    def __init__(self):
        self.code = "FUN-17"
        self.name = "Максимум соединений в запросе"
        self.description = "Не более 5 таблиц в одном запросе."
        self.severity = "WARNING"
        self.max_joins = 5

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if hasattr(module, 'original_code') and module.original_code:
            lines = module.original_code.split('\n')
            for i, line in enumerate(lines, 1):
                if 'СОЕДИНЕНИЕ' in line or 'JOIN' in line.upper():
                    join_count = line.upper().count('JOIN')
                    if join_count > self.max_joins:
                        violations.append(Violation(
                            rule_code=self.code,
                            rule_name=self.name,
                            severity=self.severity,
                            module_name=module.name,
                            line=i,
                            column=1,
                            message=f"Запрос содержит {join_count} соединений (макс. {self.max_joins})"
                        ))
        return violations