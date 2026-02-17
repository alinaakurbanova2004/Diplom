from typing import List
from Diplom.src.parser.ast_nodes import ModuleNode
from Diplom.src.rules.basic_rule import BaseRule
from Diplom.src.rules.violation import Violation


class FlagVariableNames(BaseRule):
    """
    Правило 5: Переменные-флаги должны называться по истинному значению
    Пример: ЕстьОшибки, ЭтоТоварТара, НужноОбновить
    """

    def __init__(self):
        self.code = "VAR-05"
        self.name = "Имена для переменных-флагов"
        self.description = "Переменные-флаги"
        "должны называться по истинному значению (ЕстьОшибки, ЭтоТоварТара)"
        self.severity = "INFO"

        # Хорошие префиксы для флагов
        self.good_prefixes = [
            "Есть",
            "Нет",
            "Можно",
            "Нельзя",
            "Нужно",
            "Требуется",
            "Разрешено",
            "Запрещено",
            "ЭтоАктивно",
            "ЭтоВыбрано",
            "ЭтоЗавершено",
            "Признак",
            "Флаг",
            "Состояние",
        ]

        # Плохие имена для флагов
        self.bad_flag_names = [
            "флаг",
            "признак",
            "состояние",
            "режим",
            "тип",
            "value",
            "flag",
            "status",
            "mode",
            "type",
        ]

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        for var in module.variables:
            if self._looks_like_flag(var.name) and not self._is_good_flag_name(
                var.name
            ):
                violations.append(
                    Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=var.range.start.line if var.range else 0,
                        column=var.range.start.column if var.range else 0,
                        message=f"Переменная-флаг '{var.name}' должна"
                        f"называться по истинному значению"
                        f"(например: ЕстьОшибки, ЭтоТоварТара)",
                    )
                )

        return violations

    def _looks_like_flag(self, name: str) -> bool:
        """Определяет, похоже ли имя на флаг"""
        name_lower = name.lower()

        # Проверяем по плохим именам
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
