from typing import List
from Diplom.src.parser.ast_nodes import ModuleNode
from Diplom.src.rules.basic_rule import BaseRule
from Diplom.src.rules.violation import Violation


class ProcedureLengthRule(BaseRule):
    """Процедура не должна быть слишком длинной"""

    def __init__(self):
        self.code = "FUN-03"
        self.name = "Слишком длинная процедура"
        self.description = "Процедура должна содержать не более 50 строк"
        self.severity = "WARNING"
        self.max_lines = 50

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        for proc in module.procedures:
            if proc.range:
                lines_count = proc.range.end.line - proc.range.start.line
                if lines_count > self.max_lines:
                    violations.append(
                        Violation(
                            rule_code=self.code,
                            rule_name=self.name,
                            severity=self.severity,
                            module_name=module.name,
                            line=proc.range.start.line,
                            column=proc.range.start.column,
                            message=f"Процедура '{proc.name}' слишком длинная"
                            f"({lines_count} строк)."
                            f"Рекомендуется не более {self.max_lines} строк",
                        )
                    )

        return violations
