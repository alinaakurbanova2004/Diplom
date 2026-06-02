from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class RequireAccessCheck(BaseRule):
    """
    Правило SEC-04: Проверка прав доступа перед важными операциями
    """

    def __init__(self):
        self.code = "SEC-04"
        self.name = "Проверка прав доступа"
        self.description = "Перед важными операциями проверяйте права доступа."
        self.severity = "ERROR"
        self.sensitive_operations = [
            "Удалить", "Изменить", "Записать",
            "Установить", "Заблокировать"
        ]

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if hasattr(module, 'original_code') and module.original_code:
            has_check = "ПроверитьПрава" in module.original_code or "Разрешено" in module.original_code
            if not has_check:
                lines = module.original_code.split('\n')
                for i, line in enumerate(lines, 1):
                    for op in self.sensitive_operations:
                        if op in line:
                            violations.append(Violation(
                                rule_code=self.code,
                                rule_name=self.name,
                                severity=self.severity,
                                module_name=module.name,
                                line=i,
                                column=line.find(op) + 1,
                                message=f"Операция '{op}' требует проверки прав доступа"
                            ))
        return violations
