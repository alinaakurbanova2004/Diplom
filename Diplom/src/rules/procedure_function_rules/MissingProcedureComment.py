from typing import List
from Diplom.src.parser.ast_nodes import ModuleNode
from Diplom.src.rules.basic_rule import BaseRule
from Diplom.src.rules.violation import Violation


class MissingProcedureCommentRule(BaseRule):
    """У каждой процедуры должен быть комментарий с описанием"""

    def __init__(self):
        self.code = "FUN-05"
        self.name = "Отсутствует описание процедуры"
        self.description = "Добавьте комментарий перед процедурой с описанием"
        self.severity = "INFO"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        with open(module.source_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for proc in module.procedures:
            line_before = proc.range.start.line - 2 if proc.range else 0
            if line_before >= 0:
                prev_line = lines[line_before].strip()
                if not prev_line.startswith("//"):
                    violations.append(
                        Violation(
                            rule_code=self.code,
                            rule_name=self.name,
                            severity=self.severity,
                            module_name=module.name,
                            line=proc.range.start.line if proc.range else 0,
                            column=1,
                            message=f"Процедура '{proc.name}'"
                            f"не имеет описания."
                            f"Добавьте комментарий над процедурой",
                        )
                    )

        return violations
