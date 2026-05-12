from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class WithoutUnderscorePrefix(BaseRule):
    """Правило VAR-03: Имена переменных запрещается начинать с подчеркивания"""

    def __init__(self):
        self.code = "VAR-03"
        self.name = "Запрет на подчеркивание в начале"
        self.description = (
            "Имена переменных не должны начинаться с символа подчеркивания."
        )
        self.severity = "ERROR"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        # 1. Глобальные переменные
        for var in module.variables:
            if var.name.startswith("_"):
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
                        message=f"Переменная '{var.name}' начинается с подчеркивания. Удалите подчеркивание.",
                    )
                )

        # 2. Локальные переменные в процедурах
        for proc in module.procedures:
            for var in proc.local_vars:
                if var.name.startswith("_"):
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
                            message=f"Переменная '{var.name}' в процедуре '{proc.name}' начинается с подчеркивания. Удалите подчеркивание.",
                        )
                    )

        # 3. Локальные переменные в функциях
        for func in module.functions:
            for var in func.local_vars:
                if var.name.startswith("_"):
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
                            message=f"Переменная '{var.name}' в функции '{func.name}' начинается с подчеркивания. Удалите подчеркивание.",
                        )
                    )

        return violations