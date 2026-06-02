from typing import List
import re
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class NoSecretsInLogs(BaseRule):
    """
    Правило SEC-05: Запрет на хранение конфиденциальных данных в логах
    """

    def __init__(self):
        self.code = "SEC-05"
        self.name = "Запрет на хранение секретов в логах"
        self.description = "Не записывайте пароли и токены в журнал регистрации."
        self.severity = "ERROR"
        self.secret_patterns = [
            r'пароль', r'password', r'token', r'ключ', r'secret',
            r'passwd', r'pwd', r'auth', r'credentials'
        ]

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if hasattr(module, 'original_code') and module.original_code:
            lines = module.original_code.split('\n')
            in_log_statement = False
            for i, line in enumerate(lines, 1):
                if 'ЗаписьЖурналаРегистрации' in line or 'Записать' in line:
                    in_log_statement = True
                if in_log_statement:
                    for pattern in self.secret_patterns:
                        if re.search(pattern, line, re.IGNORECASE):
                            violations.append(Violation(
                                rule_code=self.code,
                                rule_name=self.name,
                                severity=self.severity,
                                module_name=module.name,
                                line=i,
                                column=line.lower().find(pattern) + 1,
                                message="Конфиденциальные данные не должны записываться в логи"
                            ))
                    if ';' in line:
                        in_log_statement = False
        return violations