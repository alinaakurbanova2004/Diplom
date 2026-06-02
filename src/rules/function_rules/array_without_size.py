from typing import List
import re
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class ArrayWithoutSize(BaseRule):
    """
    Правило FUN-09: Запрет на использование "Массив" без указания размера
    Создание массива без размера менее производительно.
    """

    def __init__(self):
        self.code = "FUN-09"
        self.name = "Массив без указания размера"
        self.description = "Указывайте размер массива при создании."
        self.severity = "WARNING"
        self.pattern = r'Новый\s+Массив\s*\(\s*\)'

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if hasattr(module, 'original_code') and module.original_code:
            lines = module.original_code.split('\n')
            for i, line in enumerate(lines, 1):
                if re.search(self.pattern, line, re.IGNORECASE):
                    violations.append(Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=i,
                        column=line.find('Новый Массив') + 1,
                        message="Создание массива без указания размера снижает производительность. Используйте 'Новый Массив(Размер)'."
                    ))
        return violations