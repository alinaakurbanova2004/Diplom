from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class NoUnsafeFunctions(BaseRule):
    """
    Правило SEC-03: Запрет на использование небезопасных функций
    """

    def __init__(self):
        self.code = "SEC-03"
        self.name = "Запрет на использование небезопасных функций"
        self.description = "Избегайте использования потенциально опасных функций."
        self.severity = "WARNING"
        self.unsafe_functions = [
            "Выполнить", "Eval", "Вычислить",
            "ЗагрузитьИзФайла", "ЧтениеТекста"
        ]

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if hasattr(module, 'original_code') and module.original_code:
            lines = module.original_code.split('\n')
            for i, line in enumerate(lines, 1):
                for func in self.unsafe_functions:
                    if func in line:
                        violations.append(Violation(
                            rule_code=self.code,
                            rule_name=self.name,
                            severity=self.severity,
                            module_name=module.name,
                            line=i,
                            column=line.find(func) + 1,
                            message=f"Использование потенциально опасной функции '{func}'"
                        ))
        return violations
