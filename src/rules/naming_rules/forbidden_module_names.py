from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class ForbiddenModuleNames(BaseRule):
    """
    Правило VAR-07: Запрещённые имена модулей
    Имена модулей не должны содержать временные названия.
    """

    def __init__(self):
        self.code = "VAR-07"
        self.name = "Запрещённые имена модулей"
        self.description = "Имена модулей не должны содержать временные названия."
        self.severity = "ERROR"
        self.forbidden_words = ["test", "temp", "debug", "new", "tmp", "новый", "временный"]

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        module_name = module.name.lower()
        for word in self.forbidden_words:
            if word in module_name:
                violations.append(Violation(
                    rule_code=self.code,
                    rule_name=self.name,
                    severity=self.severity,
                    module_name=module.name,
                    line=1,
                    column=1,
                    message=f"Имя модуля '{module.name}' содержит запрещённое слово '{word}'"
                ))
        return violations