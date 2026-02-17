from typing import List
from Diplom.src.parser.ast_nodes import ModuleNode, VariableNode
from Diplom.src.rules.basic_rule import BaseRule
from Diplom.src.rules.violation import Violation


class MeaningfulVariable(BaseRule):

    """Правило 1: Имена переменных должны быть понятны из предметной области"""

    def __init__(self):
        self.code = "VAR-01"
        self.name = "Понятное имя переменной"
        self.description = (
            "Имя переменной должно отражать" +
            "её назначение из предметной области"
        )
        self.severity = "WARNING"

        # Список "плохих" сокращений
        self.bad_abbreviations = [
            "к",
            "ч",
            "с",
            "п",
            "р",
            "д",
            "в",
            "н",
            "т",
            "м",
            "кол",
            "кл",
            "ст",
            "стр",
            "ном",
            "сум",
            "об",
            "колво",
            "тчк",
            "знч",
            "спр",
            "док",
            "рег",
            "отч",
            "обр",
        ]

        # Список "хороших" слов-маркеров
        self.good_markers = [
            "Количество",
            "Сумма",
            "Цена",
            "Наименование",
            "Код",
            "Идентификатор",
            "Дата",
            "Время",
            "Период",
            "Статус",
        ]

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        for var in module.variables:
            if self._is_bad_variable_name(var.name):
                violations.append(
                    Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=var.range.start.line if var.range else 0,
                        column=var.range.start.column if var.range else 0,
                        message=(
                            f"Переменная '{var.name}' имеет"
                            f"непонятное назначение."
                            f"Используйте полные"
                            f"названия из предметной области")
                        )
                )

        # Проверяем локальные переменные в процедурах
        for proc in module.procedures:
            for node in proc.body:
                if isinstance(node, VariableNode):
                    if self._is_bad_variable_name(node.name):
                        violations.append(Violation(...))

        return violations

    def _is_bad_variable_name(self, name: str) -> bool:
        """Проверка, плохое ли имя переменной"""
        name_lower = name.lower()

        # Проверка на плохие сокращения
        for bad in self.bad_abbreviations:
            if (
                bad == name_lower
                or name_lower.startswith(bad + "_")
                or name_lower.endswith("_" + bad)
            ):
                return True

        # Проверка на наличие хороших маркеров
        has_good_marker = False
        for marker in self.good_markers:
            if marker.lower() in name_lower:
                has_good_marker = True
                break

        if len(name) > 10 and not has_good_marker:
            return True

        return False
