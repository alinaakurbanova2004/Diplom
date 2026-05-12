"""
Правило FUN-02: Пустые процедуры и функции запрещены
Сгенерировано автоматически. Требуется ручная доработка логики.
"""

from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class Fun02(BaseRule):
    def __init__(self):
        self.code = "FUN-02"
        self.name = "Пустые процедуры и функции запрещены"
        self.severity = "WARNING"
    
    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        # TODO: Реализовать логику проверки
        return violations
