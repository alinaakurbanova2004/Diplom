from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class NoObsoleteMethods(BaseRule):
    """
    Правило FUN-14: Запрет на использование устаревших методов
    Используйте актуальные методы вместо устаревших.
    """

    def __init__(self):
        self.code = "FUN-14"
        self.name = "Запрет на использование устаревших методов"
        self.description = "Используйте актуальные методы вместо устаревших."
        self.severity = "WARNING"
        self.obsolete_methods = [
            "НайтиПоНомеру",
            "ПолучитьЗначениеПараметра",
            "УстановитьЗначениеПараметра",
            "ЗагрузитьДанныеИзФайла",
            "СохранитьДанныеВФайл"
        ]

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if hasattr(module, 'original_code') and module.original_code:
            lines = module.original_code.split('\n')
            for i, line in enumerate(lines, 1):
                for method in self.obsolete_methods:
                    if method in line:
                        violations.append(Violation(
                            rule_code=self.code,
                            rule_name=self.name,
                            severity=self.severity,
                            module_name=module.name,
                            line=i,
                            column=line.find(method) + 1,
                            message=f"Использование устаревшего метода '{method}'. Замените на актуальный."
                        ))
        return violations