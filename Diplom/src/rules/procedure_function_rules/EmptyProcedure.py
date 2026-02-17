from typing import List
from Diplom.src.parser.ast_nodes import ModuleNode
from Diplom.src.rules.basic_rule import BaseRule
from Diplom.src.rules.violation import Violation


class EmptyProcedure(BaseRule):
    """Процедура не должна быть пустой"""

    def __init__(self):
        self.code = "FUN-02"
        self.name = "Пустые процедуры запрещены"
        self.description = "Процедура должна содержать хотя бы один оператор"
        self.severity = "WARNING"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        for proc in module.procedures:
            if not proc.body:  # пустое тело
                violations.append(
                    Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=proc.range.start.line if proc.range else 0,
                        column=proc.range.start.column if proc.range else 0,
                        message=f"Процедура '{proc.name}' пустая."
                        f"Добавьте операторы или удалите процедуру",
                    )
                )

        return violations
