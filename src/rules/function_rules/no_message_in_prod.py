from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class NoMessageInProduction(BaseRule):
    """
    Правило FUN-13: Запрет на Сообщить в продуктивном коде
    Сообщить() следует использовать только для отладки.
    """

    def __init__(self):
        self.code = "FUN-13"
        self.name = "Запрет на Сообщить в продуктивном коде"
        self.description = "Используйте Сообщить() только для отладки."
        self.severity = "WARNING"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if hasattr(module, 'original_code') and module.original_code:
            lines = module.original_code.split('\n')
            for i, line in enumerate(lines, 1):
                if 'Сообщить(' in line:
                    violations.append(Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=i,
                        column=line.find('Сообщить(') + 1,
                        message="Обнаружен вызов 'Сообщить()' в коде. Уберите перед выпуском в продуктив."
                    ))
        return violations