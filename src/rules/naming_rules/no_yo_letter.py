from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class NoYoLetter(BaseRule):
    """Правило VAR-10: Использование символа "ё" в идентификаторах (#std456)"""
    
    def __init__(self):
        self.code = "VAR-10"
        self.name = "Использование символа ё в идентификаторах"
        self.description = "Не используйте букву ё в именах переменных, процедур и функций."
        self.severity = "INFO"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        
        for var in module.variables:
            if 'ё' in var.name.lower():
                line = var.range.start.line if var.range else 0
                violations.append(Violation(
                    rule_code=self.code,
                    rule_name=self.name,
                    severity=self.severity,
                    module_name=module.name,
                    line=line,
                    column=0,
                    message=f"Переменная '{var.name}' содержит букву 'ё'. Замените на 'е'."
                ))
        
        for proc in module.procedures:
            if 'ё' in proc.name.lower():
                line = proc.range.start.line if proc.range else 0
                violations.append(Violation(
                    rule_code=self.code,
                    rule_name=self.name,
                    severity=self.severity,
                    module_name=module.name,
                    line=line,
                    column=0,
                    message=f"Процедура '{proc.name}' содержит букву 'ё'. Замените на 'е'."
                ))
        
        for func in module.functions:
            if 'ё' in func.name.lower():
                line = func.range.start.line if func.range else 0
                violations.append(Violation(
                    rule_code=self.code,
                    rule_name=self.name,
                    severity=self.severity,
                    module_name=module.name,
                    line=line,
                    column=0,
                    message=f"Функция '{func.name}' содержит букву 'ё'. Замените на 'е'."
                ))
                
        return violations