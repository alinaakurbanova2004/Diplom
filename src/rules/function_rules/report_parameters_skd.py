from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class ReportParametersSKD(BaseRule):
    def __init__(self):
        self.code = "FUN-21"
        self.name = "Применение параметров отчета в СКД"
        self.description = "Параметры отчета должны явно применяться в схеме компоновки данных."
        self.severity = "INFO"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if hasattr(module, 'original_code') and module.original_code:
            lines = module.original_code.split('\n')
            for i, line in enumerate(lines, 1):
                if 'СхемаКомпоновкиДанных' in line:
                    if 'Параметр' in line and 'УстановитьПараметр' not in line:
                        violations.append(Violation(
                            rule_code=self.code,
                            rule_name=self.name,
                            severity=self.severity,
                            module_name=module.name,
                            line=i,
                            column=1,
                            message="Убедитесь, что параметры отчета явно установлены в СКД перед выводом."
                        ))
        return violations
