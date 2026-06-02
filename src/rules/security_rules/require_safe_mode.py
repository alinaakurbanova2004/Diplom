from typing import List
import re
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class RequireSafeMode(BaseRule):
    """
    Правило SEC-07: Перед вызовом Выполнить/Вычислить должен быть включен безопасный режим
    """

    def __init__(self):
        self.code = "SEC-07"
        self.name = "Отсутствует включение безопасного режима перед Выполнить/Вычислить"
        self.description = "Перед вызовом Выполнить() или Вычислить() необходимо установить безопасный режим."
        self.severity = "ERROR"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if not hasattr(module, 'original_code') or not module.original_code:
            return violations

        lines = module.original_code.split('\n')
        for i, line in enumerate(lines, 1):
            if 'Выполнить(' in line or 'Вычислить(' in line:
                # Проверяем, был ли безопасный режим включен ранее
                prev_lines = '\n'.join(lines[max(0, i-10):i])
                if 'УстановитьБезопасныйРежим' not in prev_lines:
                    violations.append(Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=i,
                        column=line.find('Выполнить') + 1,
                        message="Перед вызовом Выполнить/Вычислить необходимо включить безопасный режим."
                    ))
        return violations