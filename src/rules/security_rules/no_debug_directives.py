from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class NoDebugDirectives(BaseRule):
    """
    Правило SEC-07: Запрет на использование отладочных директив в продуктивном коде
    """

    def __init__(self):
        self.code = "SEC-07"
        self.name = "Запрет на отладочные директивы"
        self.description = "Удалите отладочные директивы перед выпуском."
        self.severity = "WARNING"
        self.debug_directives = [
            "&НаКлиенте", "&НаСервере", "&НаКлиентеНаСервере",
            "&Вместо", "&Перед", "&После", "&Заголовок"
        ]

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if hasattr(module, 'original_code') and module.original_code:
            lines = module.original_code.split('\n')
            for i, line in enumerate(lines, 1):
                for directive in self.debug_directives:
                    if directive in line:
                        violations.append(Violation(
                            rule_code=self.code,
                            rule_name=self.name,
                            severity=self.severity,
                            module_name=module.name,
                            line=i,
                            column=line.find(directive) + 1,
                            message=f"Отладочная директива '{directive}' не должна присутствовать в продуктивном коде"
                        ))
        return violations
