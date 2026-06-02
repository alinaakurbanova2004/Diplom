from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class MissingProcedureComment(BaseRule):
    """
    Правило FUN-05: Экспортные методы должны иметь комментарий
    """

    def __init__(self):
        self.code = "FUN-05"
        self.name = "Отсутствует комментарий у экспортного метода"
        self.description = "Экспортные процедуры и функции должны иметь комментарий с описанием."
        self.severity = "WARNING"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if not hasattr(module, 'original_code') or not module.original_code:
            return violations

        lines = module.original_code.split('\n')

        # Ищем все экспортные процедуры и функции
        for i, line in enumerate(lines, 1):
            if 'Экспорт' in line and ('Процедура' in line or 'Функция' in line):
                # Проверяем предыдущую строку
                prev_line = lines[i-2].strip() if i >= 2 else ''
                if not prev_line.startswith('//'):
                    violations.append(Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=i,
                        column=1,
                        message="Добавьте комментарий перед экспортной процедурой/функцией"
                    ))
        return violations