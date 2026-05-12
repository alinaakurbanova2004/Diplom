"""
Правило FUN-05: Отсутствует описание процедуры или функции
Сгенерировано автоматически. Требуется ручная доработка логики.
"""

from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class Fun05(BaseRule):
    def __init__(self):
        self.code = "FUN-05"
        self.name = "Отсутствует описание процедуры или функции"
        self.severity = "INFO"
    
    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        # TODO: Реализовать логику проверки
        return violations
