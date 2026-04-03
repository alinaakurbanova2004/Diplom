from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class MeaningfulVariable(BaseRule):
    """Правило VAR-01: Понятное имя переменной"""

    def __init__(self):
        self.code = "VAR-01"
        self.name = "Понятное имя переменной"
        self.description = (
            "Имя переменной должно отражать её назначение из предметной области"
        )
        self.severity = "WARNING"

        self.bad_abbreviations = [
            "к", "ч", "с", "п", "р", "д", "в", "н", "т", "м",
            "кол", "кл", "ст", "стр", "ном", "сум", "об", "колво",
            "тчк", "знч", "спр", "док", "рег", "отч", "обр",
        ]

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        # 1. Глобальные переменные
        for var in module.variables:
            if self._is_bad_variable_name(var.name):
                line = var.range.start.line if var.range else 0
                col = var.range.start.column if var.range else 0
                violations.append(self._create_violation(var, module, None, line, col))

        # 2. Локальные переменные в процедурах
        for proc in module.procedures:
            for var in proc.local_vars:
                if self._is_bad_variable_name(var.name):
                    line = var.range.start.line if var.range else 0
                    col = var.range.start.column if var.range else 0
                    violations.append(self._create_violation(var, module, proc.name, line, col))

        # 3. Локальные переменные в функциях
        for func in module.functions:
            for var in func.local_vars:
                if self._is_bad_variable_name(var.name):
                    line = var.range.start.line if var.range else 0
                    col = var.range.start.column if var.range else 0
                    violations.append(self._create_violation(var, module, func.name, line, col))

        return violations

    def _is_bad_variable_name(self, name: str) -> bool:
        name_lower = name.lower()

        # Слишком короткие имена (1-2 символа)
        if len(name) <= 2:
            return True
        
        # Проверка на плохие сокращения
        for bad in self.bad_abbreviations:
            if (bad == name_lower
                or name_lower.startswith(bad + "_")
                or name_lower.endswith("_" + bad)):
                return True
            if bad in name_lower.split('_'):
                return True

        return False

    def _create_violation(self, var, module, context=None, line=0, col=0):
        context_info = f" в {context}" if context else ""
        return Violation(
            rule_code=self.code,
            rule_name=self.name,
            severity=self.severity,
            module_name=module.name,
            line=line,      # ← используем переданное значение
            column=col,     # ← используем переданное значение
            message=(
                f"Переменная '{var.name}'{context_info} имеет "
                f"непонятное назначение. Используйте полные "
                f"названия из предметной области"
            ),
        )