from dataclasses import dataclass


@dataclass
class Violation:
    rule_code: str
    rule_name: str
    severity: str
    module_name: str
    line: int
    column: int
    message: str
    code_snippet: str = ""
