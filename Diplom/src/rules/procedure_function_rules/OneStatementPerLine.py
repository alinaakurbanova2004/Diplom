from typing import List
from Diplom.src.parser.ast_nodes import ModuleNode
from Diplom.src.rules.basic_rule import BaseRule
from Diplom.src.rules.violation import Violation


class OneStatementPerLine(BaseRule):
    """В одной строке должен быть только один оператор"""

    def __init__(self):
        self.code = "FUN-01"
        self.name = "Один оператор в строке"
        self.description = "Не пишите несколько операторов в одной строке"
        self.severity = "WARNING"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        # Анализируем исходный код по строкам
        with open(module.source_file, "r", encoding="utf-8") as f:
            lines = f.readlines()

        for i, line in enumerate(lines, 1):
            line = line.strip()
            if line.count(";") > 1:
                violations.append(
                    Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=i,
                        column=1,
                        message="Строка содержит"
                        "несколько операторов (разделите на отдельные строки)",
                    )
                )

        return violations
