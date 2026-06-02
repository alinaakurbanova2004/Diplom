from typing import List
import re
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class NoPasswordsInCode(BaseRule):
    def __init__(self):
        self.code = "SEC-01"
        self.name = "Запрет на хранение паролей в коде"
        self.description = "Не храните пароли и секретные ключи в исходном коде."
        self.severity = "ERROR"
        self.patterns = [
            r'пароль\s*=\s*["\']([^"\']+)["\']',
            r'password\s*=\s*["\']([^"\']+)["\']',
            r'pwd\s*=\s*["\']([^"\']+)["\']',
            r'token\s*=\s*["\']([^"\']+)["\']',
            r'secret\s*=\s*["\']([^"\']+)["\']',
        ]

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if hasattr(module, 'original_code') and module.original_code:
            lines = module.original_code.split('\n')
            for i, line in enumerate(lines, 1):
                for pattern in self.patterns:
                    if re.search(pattern, line, re.IGNORECASE):
                        violations.append(Violation(
                            rule_code=self.code,
                            rule_name=self.name,
                            severity=self.severity,
                            module_name=module.name,
                            line=i,
                            column=1,
                            message="Обнаружена возможная утечка пароля или секретного ключа. Используйте защищённое хранилище."
                        ))
        return violations
