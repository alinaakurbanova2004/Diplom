from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class CommentFormat(BaseRule):
    """
    Правило VAR-09: Неправильное оформление комментария
    Между // и текстом комментария должен быть пробел.
    """

    def __init__(self):
        self.code = "VAR-09"
        self.name = "Неправильное оформление комментария"
        self.description = "Между // и текстом комментария должен быть пробел."
        self.severity = "INFO"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if not hasattr(module, 'original_code') or not module.original_code:
            return violations

        lines = module.original_code.split('\n')
        for i, line in enumerate(lines, 1):
            stripped = line.strip()
            if stripped.startswith('//') and not stripped.startswith('///'):
                # Проверяем, есть ли пробел после //
                if len(stripped) > 2 and stripped[2] != ' ':
                    violations.append(Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=i,
                        column=line.find('//') + 3,
                        message="Вставьте пробел между '//' и текстом комментария."
                    ))
        return violations