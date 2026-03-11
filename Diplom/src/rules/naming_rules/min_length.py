from typing import List
from src.parser.ast_nodes import ModuleNode, ProcedureNode, VariableNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class VariableMinLength(BaseRule):
    """
    Правило 4: Имена переменных не должны состоять из одного символа
    Исключение: счетчики циклов
    """

    def __init__(self):
        self.code = "VAR-04"
        self.name = "Минимальная длина имени"
        self.description = "Имена переменных должны"
        "быть длиннее одного символа (исключение: счетчики циклов)"
        self.severity = "WARNING"

        # Допустимые односимвольные имена для счетчиков
        self.loop_counters = ["i", "j", "k", "n", "m"]

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        # Проверяем глобальные переменные модуля
        for var in module.variables:
            if len(var.name) == 1 and var.name not in self.loop_counters:
                violations.append(self._create_violation(var, module))

        # Проверяем локальные переменные в процедурах
        for proc in module.procedures:
            for var in proc.local_vars:
                if len(var.name) == 1 and var.name not in self.loop_counters:
                    violations.append(self._create_violation(var, module, proc.name))

        # Проверяем локальные переменные в функциях
        for func in module.functions:
            for var in func.local_vars:
                if len(var.name) == 1 and var.name not in self.loop_counters:
                    violations.append(self._create_violation(var, module, func.name))
        return violations

    def _create_violation(self, var, module, context=None):
        context_info = f" в {context}" if context else ""
        return Violation(
            rule_code=self.code,
            rule_name=self.name,
            severity=self.severity,
            module_name=module.name,
            line=var.range.start.line if var.range else 0,
            column=var.range.start.column if var.range else 0,
            message=(
                f"Переменная '{var.name}'{context_info} состоит из одного символа. "
                f"Дайте ей осмысленное имя."
            ),
        )
