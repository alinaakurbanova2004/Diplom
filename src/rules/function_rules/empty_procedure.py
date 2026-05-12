from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class EmptyProcedure(BaseRule):
    """Правило FUN-02: Пустые процедуры и функции запрещены"""

    def __init__(self):
        self.code = "FUN-02"
        self.name = "Пустые процедуры и функции запрещены"
        self.description = "Процедура или функция должна содержать хотя бы один оператор."
        self.severity = "WARNING"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        # 1. Проверяем процедуры
        for proc in module.procedures:
            if not proc.body:  # пустое тело
                line = proc.range.start.line if proc.range else 0
                col = proc.range.start.column if proc.range else 0
                violations.append(
                    Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=line,
                        column=col,
                        message=f"Процедура '{proc.name}' пустая. Добавьте операторы или удалите процедуру.",
                    )
                )

        # 2. Проверяем функции
        for func in module.functions:
            if not func.body:  # пустое тело
                line = func.range.start.line if func.range else 0
                col = func.range.start.column if func.range else 0
                violations.append(
                    Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=line,
                        column=col,
                        message=f"Функция '{func.name}' пустая. Добавьте операторы или удалите функцию.",
                    )
                )

        return violations