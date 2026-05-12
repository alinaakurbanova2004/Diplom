"""
Правило VAR-01: Понятное имя переменной
Сгенерировано автоматически. Требуется ручная доработка логики.
"""

from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class Var01(BaseRule):
    def __init__(self):
        self.code = "VAR-01"
        self.name = "Понятное имя переменной"
        self.severity = "WARNING"
    
    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        # TODO: Реализовать логику проверки
        return violations
