from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class MaxLineLength(BaseRule):
    """
    Правило FUN-12: Максимальная длина строки
    Проверяет, что длина строки не превышает заданного значения.
    """

    def __init__(self):
        self.code = "FUN-12"
        self.name = "Максимальная длина строки"
        self.description = "Длина строки не должна превышать 120 символов."
        self.severity = "INFO"
        self.max_length = 120

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if hasattr(module, 'original_code') and module.original_code:
            lines = module.original_code.split('\n')
            for i, line in enumerate(lines, 1):
                line_stripped = line.strip()
                if not line_stripped or line_stripped.startswith('//'):
                    continue
                if len(line) > self.max_length:
                    violations.append(Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=i,
                        column=self.max_length + 1,
                        message=f"Строка слишком длинная ({len(line)} символов, макс. {self.max_length})"
                    ))
        return violations