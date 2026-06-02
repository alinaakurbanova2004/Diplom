from typing import List
import re
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class NoTranslitNames(BaseRule):
    """
    Правило VAR-08: Запрет на использование транслита в именах
    Имена переменных, процедур и функций должны быть на русском языке.
    """

    def __init__(self):
        self.code = "VAR-08"
        self.name = "Запрет на использование транслита"
        self.description = "Используйте русские осмысленные имена вместо транслитерации."
        self.severity = "WARNING"
        # Латинские буквы (признак транслита)
        self.latin_pattern = re.compile(r'[a-zA-Z]')
        # Русские буквы
        self.russian_pattern = re.compile(r'[а-яА-ЯёЁ]')

    def _is_translit(self, name: str) -> bool:
        """Проверяет, похоже ли имя на транслит"""
        if len(name) < 3:
            return False
        # Если есть латинские буквы и нет русских → это транслит
        has_latin = bool(self.latin_pattern.search(name))
        has_russian = bool(self.russian_pattern.search(name))
        return has_latin and not has_russian

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        # 1. Глобальные переменные
        for var in module.variables:
            if self._is_translit(var.name):
                line = var.range.start.line if var.range else 0
                col = var.range.start.column if var.range else 0
                violations.append(Violation(
                    rule_code=self.code,
                    rule_name=self.name,
                    severity=self.severity,
                    module_name=module.name,
                    line=line,
                    column=col,
                    message=f"Переменная '{var.name}' использует транслит. Используйте русское имя."
                ))

        # 2. Процедуры
        for proc in module.procedures:
            if self._is_translit(proc.name):
                line = proc.range.start.line if proc.range else 0
                col = proc.range.start.column if proc.range else 0
                violations.append(Violation(
                    rule_code=self.code,
                    rule_name=self.name,
                    severity=self.severity,
                    module_name=module.name,
                    line=line,
                    column=col,
                    message=f"Процедура '{proc.name}' использует транслит. Используйте русское имя."
                ))

        # 3. Функции
        for func in module.functions:
            if self._is_translit(func.name):
                line = func.range.start.line if func.range else 0
                col = func.range.start.column if func.range else 0
                violations.append(Violation(
                    rule_code=self.code,
                    rule_name=self.name,
                    severity=self.severity,
                    module_name=module.name,
                    line=line,
                    column=col,
                    message=f"Функция '{func.name}' использует транслит. Используйте русское имя."
                ))

        # 4. Параметры процедур и функций
        for proc in module.procedures:
            for param in proc.parameters:
                if self._is_translit(param.name):
                    line = param.range.start.line if param.range else 0
                    col = param.range.start.column if param.range else 0
                    violations.append(Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=line,
                        column=col,
                        message=f"Параметр '{param.name}' в процедуре '{proc.name}' использует транслит."
                    ))

        for func in module.functions:
            for param in func.parameters:
                if self._is_translit(param.name):
                    line = param.range.start.line if param.range else 0
                    col = param.range.start.column if param.range else 0
                    violations.append(Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=line,
                        column=col,
                        message=f"Параметр '{param.name}' в функции '{func.name}' использует транслит."
                    ))

        return violations