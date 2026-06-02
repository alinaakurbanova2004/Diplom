from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class MaxLocalVariables(BaseRule):
    """
    Правило FUN-08: Слишком много локальных переменных
    Проверяет, что в процедуре/функции не более заданного количества локальных переменных.
    """

    def __init__(self):
        self.code = "FUN-08"
        self.name = "Слишком много локальных переменных"
        self.description = "В процедуре/функции не должно быть более 10 локальных переменных."
        self.severity = "WARNING"
        self.max_vars = 10

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        for proc in module.procedures:
            if len(proc.local_vars) > self.max_vars:
                line = proc.range.start.line if proc.range else 0
                violations.append(Violation(
                    rule_code=self.code,
                    rule_name=self.name,
                    severity=self.severity,
                    module_name=module.name,
                    line=line,
                    column=0,
                    message=f"Процедура '{proc.name}' содержит {len(proc.local_vars)} локальных переменных (макс. {self.max_vars})"
                ))
        for func in module.functions:
            if len(func.local_vars) > self.max_vars:
                line = func.range.start.line if func.range else 0
                violations.append(Violation(
                    rule_code=self.code,
                    rule_name=self.name,
                    severity=self.severity,
                    module_name=module.name,
                    line=line,
                    column=0,
                    message=f"Функция '{func.name}' содержит {len(func.local_vars)} локальных переменных (макс. {self.max_vars})"
                ))
        return violations