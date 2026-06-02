from typing import List
from src.parser.ast_nodes import ModuleNode, IfStatementNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class MaxConditionsInIf(BaseRule):
    def __init__(self):
        self.code = "FUN-16"
        self.name = "Максимум условий в If"
        self.description = "Не более 5 веток ИначеЕсли в одном условии."
        self.severity = "WARNING"
        self.max_branches = 5

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        for proc in module.procedures:
            for node in proc.body:
                if isinstance(node, IfStatementNode):
                    branches = 1 + len(node.elif_branches)
                    if branches > self.max_branches:
                        line = node.range.start.line if node.range else 0
                        violations.append(Violation(
                            rule_code=self.code,
                            rule_name=self.name,
                            severity=self.severity,
                            module_name=module.name,
                            line=line,
                            column=0,
                            message=f"Условие содержит {branches} веток (макс. {self.max_branches})"
                        ))
        return violations