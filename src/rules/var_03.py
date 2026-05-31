"""
Правило VAR-03: Запрет на подчеркивание в начале
Сгенерировано автоматически. Требуется ручная доработка логики.
"""

from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class Var03(BaseRule):
    def __init__(self):
        self.code = "VAR-03"
        self.name = "Запрет на подчеркивание в начале"
        self.severity = "INFO"
    
    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        # TODO: Реализовать логику проверки
        return violations
