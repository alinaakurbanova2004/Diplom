from typing import List
from src.parser.ast_nodes import ModuleNode, WhileLoopNode, ForLoopNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class NoInfiniteLoops(BaseRule):
    def __init__(self):
        self.code = "FUN-22"
        self.name = "Запрет на бесконечные циклы"
        self.description = "Убедитесь, что цикл имеет условие выхода."
        self.severity = "ERROR"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if hasattr(module, 'original_code') and module.original_code:
            lines = module.original_code.split('\n')
            for i, line in enumerate(lines, 1):
                if 'Цикл' in line and 'Пока Истина' in line:
                    violations.append(Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=i,
                        column=1,
                        message="Обнаружен потенциально бесконечный цикл 'Пока Истина'"
                    ))
        return violations