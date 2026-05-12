"""
Правило FUN-03: Слишком длинная процедура
Сгенерировано автоматически. Требуется ручная доработка логики.
"""

from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class Fun03(BaseRule):
    def __init__(self):
        self.code = "FUN-03"
        self.name = "Слишком длинная процедура"
        self.severity = "WARNING"
    
    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        # TODO: Реализовать логику проверки
        return violations
