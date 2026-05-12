"""
Правило FUN-04: Слишком много параметров
Сгенерировано автоматически. Требуется ручная доработка логики.
"""

from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class Fun04(BaseRule):
    def __init__(self):
        self.code = "FUN-04"
        self.name = "Слишком много параметров"
        self.severity = "WARNING"
    
    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        # TODO: Реализовать логику проверки
        return violations
