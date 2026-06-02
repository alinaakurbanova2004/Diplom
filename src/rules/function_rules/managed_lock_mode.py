from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class ManagedLockMode(BaseRule):
    """Правило FUN-18: Отказ от использования УправляемыйРежимБлокировки"""
    
    def __init__(self):
        self.code = "FUN-18"
        self.name = "Отказ от использования УправляемыйРежимБлокировки"
        self.description = "Следует использовать управляемый режим блокировки."
        self.severity = "WARNING"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if not hasattr(module, 'original_code') or not module.original_code:
            return violations
            
        if 'УправляемыйРежимБлокировки' in module.original_code:
            violations.append(Violation(
                rule_code=self.code,
                rule_name=self.name,
                severity=self.severity,
                module_name=module.name,
                line=1,
                column=1,
                message="Рекомендуется использовать управляемый режим блокировки вместо автоматического."
            ))
        return violations