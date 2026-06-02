from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class RequireAuditLog(BaseRule):
    """
    Правило SEC-06: Обязательное логирование важных действий
    """

    def __init__(self):
        self.code = "SEC-06"
        self.name = "Обязательное логирование важных действий"
        self.description = "Важные действия должны быть записаны в журнал регистрации."
        self.severity = "WARNING"
        self.important_actions = [
            "Удалить", "Изменить", "Создать", "Установить",
            "Заблокировать", "Разблокировать", "Экспорт"
        ]

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if hasattr(module, 'original_code') and module.original_code:
            has_log = "ЗаписьЖурналаРегистрации" in module.original_code
            lines = module.original_code.split('\n')
            for i, line in enumerate(lines, 1):
                for action in self.important_actions:
                    if action in line and not has_log:
                        violations.append(Violation(
                            rule_code=self.code,
                            rule_name=self.name,
                            severity=self.severity,
                            module_name=module.name,
                            line=i,
                            column=line.find(action) + 1,
                            message=f"Действие '{action}' должно быть залогировано"
                        ))
        return violations