from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class ForbiddenChars(BaseRule):
    """
    Правило VAR-06: Запрещённые символы в имени переменной
    Имена переменных не должны содержать специальные символы.
    """

    def __init__(self):
        self.code = "VAR-06"
        self.name = "Запрещённые символы в имени переменной"
        self.description = "Имена переменных не должны содержать запрещённые символы."
        self.severity = "ERROR"
        self.forbidden_chars = ["№", "%", "$", "@", "!", "&", "*", "(", ")", "[", "]", "{", "}", "|", "\\", "/", "?"]

    def _has_forbidden_chars(self, name: str) -> bool:
        for ch in self.forbidden_chars:
            if ch in name:
                return True
        return False

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        for var in module.variables:
            if self._has_forbidden_chars(var.name):
                line = var.range.start.line if var.range else 0
                violations.append(Violation(
                    rule_code=self.code,
                    rule_name=self.name,
                    severity=self.severity,
                    module_name=module.name,
                    line=line,
                    column=0,
                    message=f"Переменная '{var.name}' содержит запрещённый символ"
                ))

        for proc in module.procedures:
            for var in proc.local_vars:
                if self._has_forbidden_chars(var.name):
                    line = var.range.start.line if var.range else 0
                    violations.append(Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=line,
                        column=0,
                        message=f"Переменная '{var.name}' в процедуре '{proc.name}' содержит запрещённый символ"
                    ))

        for func in module.functions:
            for var in func.local_vars:
                if self._has_forbidden_chars(var.name):
                    line = var.range.start.line if var.range else 0
                    violations.append(Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=line,
                        column=0,
                        message=f"Переменная '{var.name}' в функции '{func.name}' содержит запрещённый символ"
                    ))

        return violations