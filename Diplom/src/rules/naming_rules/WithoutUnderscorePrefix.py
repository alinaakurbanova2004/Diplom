from typing import List
from Diplom.src.parser.ast_nodes import ModuleNode
from Diplom.src.rules.basic_rule import BaseRule
from Diplom.src.rules.violation import Violation


class WithoutUnderscorePrefix(BaseRule):
    """Правило 3: Имена переменных запрещается начинать с подчеркивания"""

    def __init__(self):
        self.code = "VAR-03"
        self.name = "Запрет на подчеркивание в начале"
        self.description = (
            "Имена переменных не должны начинаться с символа подчеркивания"
        )
        self.severity = "ERROR"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        for var in module.variables:
            if var.name.startswith("_"):
                violations.append(
                    Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=var.range.start.line if var.range else 0,
                        column=var.range.start.column if var.range else 0,
                        message=f"Переменная '{var.name}'"
                        f"начинается с подчеркивания. Удалите подчеркивание.",
                    )
                )

        return violations
