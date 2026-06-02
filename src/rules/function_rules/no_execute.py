from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class NoExecute(BaseRule):
    """
    Правило FUN-13: Запрет на использование Выполнить
    Использование Выполнить может быть небезопасным и снижать производительность.
    """

    def __init__(self):
        self.code = "FUN-13"
        self.name = "Запрет на использование Выполнить"
        self.description = "Использование Выполнить может быть небезопасным."
        self.severity = "ERROR"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if hasattr(module, 'original_code') and module.original_code:
            lines = module.original_code.split('\n')
            for i, line in enumerate(lines, 1):
                if 'Выполнить(' in line:
                    violations.append(Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=i,
                        column=line.find('Выполнить(') + 1,
                        message="Использование 'Выполнить' не рекомендуется из соображений безопасности."
                    ))
        return violations