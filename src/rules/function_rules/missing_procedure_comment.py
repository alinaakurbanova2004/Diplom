from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class MissingProcedureComment(BaseRule):
    """Правило FUN-05: У каждой процедуры и функции должен быть комментарий с описанием"""

    def __init__(self):
        self.code = "FUN-05"
        self.name = "Отсутствует описание процедуры или функции"
        self.description = "Добавьте комментарий перед процедурой или функцией с описанием."
        self.severity = "INFO"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        
        # Получаем исходный код напрямую из модуля
        if not hasattr(module, 'original_code') or not module.original_code:
            return violations
        
        lines = module.original_code.split('\n')
        
        # Проверяем процедуры
        for proc in module.procedures:
            if proc.range and proc.range.start.line:
                line_before = proc.range.start.line - 2  # строка перед объявлением
                if 0 <= line_before < len(lines):
                    prev_line = lines[line_before].strip()
                    if not prev_line.startswith("//"):
                        violations.append(
                            Violation(
                                rule_code=self.code,
                                rule_name=self.name,
                                severity=self.severity,
                                module_name=module.name,
                                line=proc.range.start.line,
                                column=1,
                                message=f"Процедура '{proc.name}' не имеет описания. Добавьте комментарий над процедурой.",
                            )
                        )
        
        # Проверяем функции
        for func in module.functions:
            if func.range and func.range.start.line:
                line_before = func.range.start.line - 2  # строка перед объявлением
                if 0 <= line_before < len(lines):
                    prev_line = lines[line_before].strip()
                    if not prev_line.startswith("//"):
                        violations.append(
                            Violation(
                                rule_code=self.code,
                                rule_name=self.name,
                                severity=self.severity,
                                module_name=module.name,
                                line=func.range.start.line,
                                column=1,
                                message=f"Функция '{func.name}' не имеет описания. Добавьте комментарий над функцией.",
                            )
                        )
        
        return violations