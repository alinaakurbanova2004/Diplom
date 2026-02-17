# Пример базового класса
from typing import List
from Diplom.src.parser.ast_nodes import ModuleNode
from Diplom.src.rules.violation import Violation


class BaseRule:
    def __init__(self):
        self.code = ""  # Код правила (например, "STD-01-01")
        self.name = ""  # Название правила
        self.description = ""  # Описание
        self.severity = "INFO"  # INFO, WARNING, ERROR, CRITICAL

    def check(self, module: ModuleNode) -> List[Violation]:
        """Проверяет модуль и возвращает список нарушений"""
        pass
