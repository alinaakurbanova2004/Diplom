from typing import List
from Diplom.src.parser.ast_nodes import ModuleNode
from Diplom.src.rules.basic_rule import BaseRule
from Diplom.src.rules.violation import Violation


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

        for var in module.variables:
            if not self._is_correct_camelcase(var.name):
                violations.append(
                    Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=var.range.start.line if var.range else 0,
                        column=var.range.start.column if var.range else 0,
                        message=f"Переменная '{var.name}'"
                        f"должна быть в CamelCase:"
                        f"слова слитно, каждое с большой буквы",
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
