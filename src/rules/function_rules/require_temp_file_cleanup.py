from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class RequireTempFileCleanup(BaseRule):
    """
    Правило FUN-19: Отсутствует удаление временного файла после использования
    """

    def __init__(self):
        self.code = "FUN-19"
        self.name = "Отсутствует удаление временного файла после использования"
        self.description = "Временные файлы должны быть удалены после использования."
        self.severity = "WARNING"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        if not hasattr(module, 'original_code') or not module.original_code:
            return violations

        lines = module.original_code.split('\n')
        for i, line in enumerate(lines, 1):
            if 'ПолучитьИмяВременногоФайла' in line:
                # Ищем вызов УдалитьФайлы в следующих строках
                following = '\n'.join(lines[i:i+20])
                if 'УдалитьФайлы' not in following:
                    violations.append(Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=i,
                        column=1,
                        message="Временный файл должен быть удален после использования (УдалитьФайлы)."
                    ))
        return violations