# security_rules/no_http_connection.py
from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class NoHttpConnection(BaseRule):
    def __init__(self):
        self.code = "SEC-02"
        self.name = "Запрет на использование HTTP-соединений"
        self.description = "Используйте HTTPS для безопасной передачи данных."
        self.severity = "WARNING"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if hasattr(module, 'original_code') and module.original_code:
            lines = module.original_code.split('\n')
            for i, line in enumerate(lines, 1):
                if 'http://' in line.lower() and 'HTTPСоединение' in line:
                    violations.append(Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=i,
                        column=line.lower().find('http://') + 1,
                        message="Использование HTTP-соединения небезопасно. Используйте HTTPS."
                    ))
        return violations