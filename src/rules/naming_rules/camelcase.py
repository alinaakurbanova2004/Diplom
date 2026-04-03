from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class CamelCase(BaseRule):
    """Правило 2: Составные имена пишутся
    слитно, каждое слово с большой буквы"""

    def __init__(self):
        self.code = "VAR-02"
        self.name = "CamelCase для составных имен"
        self.description = (
            "Составные имена пишутся слитно, каждое слово с большой буквы"
        )
        self.severity = "WARNING"

        # Предлоги и местоимения, которые тоже пишутся с большой
        self.prepositions = ["С", "В", "На", "По",
                             "Из", "У", "К", "О", "Об", "Без"]

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        # 1. Глобальные переменные
        for var in module.variables:
            if not self._is_correct_camelcase(var.name):
                line = var.range.start.line if var.range else 0
                col = var.range.start.column if var.range else 0
                violations.append(
                    Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=line,
                        column=col,
                        message=f"Переменная '{var.name}' должна быть в CamelCase: слова слитно, каждое с большой буквы",
                    )
                )

        # 2. Локальные переменные в процедурах
        for proc in module.procedures:
            for var in proc.local_vars:
                if not self._is_correct_camelcase(var.name):
                    line = var.range.start.line if var.range else 0
                    col = var.range.start.column if var.range else 0
                    violations.append(
                        Violation(
                            rule_code=self.code,
                            rule_name=self.name,
                            severity=self.severity,
                            module_name=module.name,
                            line=line,
                            column=col,
                            message=f"Переменная '{var.name}' в процедуре '{proc.name}' должна быть в CamelCase: слова слитно, каждое с большой буквы",
                        )
                    )

        # 3. Локальные переменные в функциях
        for func in module.functions:
            for var in func.local_vars:
                if not self._is_correct_camelcase(var.name):
                    line = var.range.start.line if var.range else 0
                    col = var.range.start.column if var.range else 0
                    violations.append(
                        Violation(
                            rule_code=self.code,
                            rule_name=self.name,
                            severity=self.severity,
                            module_name=module.name,
                            line=line,
                            column=col,
                            message=f"Переменная '{var.name}' в функции '{func.name}' должна быть в CamelCase: слова слитно, каждое с большой буквы",
                        )
                    )

        return violations

    def _is_correct_camelcase(self, name: str) -> bool:
        if not name or name[0].islower():
            return False

        # Не должно быть пробелов и подчеркиваний
        if " " in name or "_" in name:
            return False

        # Должна быть хотя бы одна заглавная внутри (если имя составное)
        if len(name) > 1 and not any(c.isupper() for c in name[1:]):
            return True

        return True
