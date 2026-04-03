from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class FlagVariableNames(BaseRule):
    """
    Правило VAR-05: Переменные-флаги должны называться по истинному значению
    Пример: ЕстьОшибки, ЭтоТоварТара, НужноОбновить
    """

    def __init__(self):
        self.code = "VAR-05"
        self.name = "Имена для переменных-флагов"
        self.description = (
            "Переменные-флаги должны называться по истинному значению "
            "(ЕстьОшибки, ЭтоТоварТара, НужноОбновить)"
        )
        self.severity = "INFO"

        # Хорошие префиксы для флагов
        self.good_prefixes = [
            "Есть", "Нет", "Можно", "Нельзя", "Нужно",
            "Требуется", "Разрешено", "Запрещено",
            "ЭтоАктивно", "ЭтоВыбрано", "ЭтоЗавершено",
            "Признак", "Флаг", "Состояние"
        ]

        # Плохие имена для флагов
        self.bad_flag_names = [
            "флаг", "признак", "состояние", "режим", "тип",
            "value", "flag", "status", "mode", "type"
        ]

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        # 1. Глобальные переменные
        for var in module.variables:
            if self._looks_like_flag(var.name) and not self._is_good_flag_name(var.name):
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
                        message=f"Переменная-флаг '{var.name}' должна называться по истинному значению (например: ЕстьОшибки, ЭтоТоварТара)",
                    )
                )

        # 2. Локальные переменные в процедурах
        for proc in module.procedures:
            for var in proc.local_vars:
                if self._looks_like_flag(var.name) and not self._is_good_flag_name(var.name):
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
                            message=f"Переменная-флаг '{var.name}' в процедуре '{proc.name}' должна называться по истинному значению (например: ЕстьОшибки, ЭтоТоварТара)",
                        )
                    )

        # 3. Локальные переменные в функциях
        for func in module.functions:
            for var in func.local_vars:
                if self._looks_like_flag(var.name) and not self._is_good_flag_name(var.name):
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
                            message=f"Переменная-флаг '{var.name}' в функции '{func.name}' должна называться по истинному значению (например: ЕстьОшибки, ЭтоТоварТара)",
                        )
                    )

        return violations

    def _looks_like_flag(self, name: str) -> bool:
        """Определяет, похоже ли имя на флаг"""
        name_lower = name.lower()
        for bad in self.bad_flag_names:
            if bad in name_lower:
                return True
        return False

    def _is_good_flag_name(self, name: str) -> bool:
        """Проверяет, хорошее ли имя для флага"""
        for prefix in self.good_prefixes:
            if name.startswith(prefix):
                return True
        return False