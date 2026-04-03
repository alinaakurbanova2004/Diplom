from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation

class MissingProcedureComment(BaseRule):
    """Правило FUN-05: У каждой процедуры и функции должен быть комментарий с описанием"""

    def __init__(self):
        self.code = "FUN-05"
        self.name = "Отсутствует описание процедуры или функции"
        self.description = "Добавьте комментарий перед процедурой или функцией с описанием"
        self.severity = "INFO"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        
        if not hasattr(module, 'source_file') or not module.source_file:
            print("⚠️ Нет информации о файле")
            return violations
        
        # Читаем файл
        try:
            with open(module.source_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            print(f"⚠️ Не удалось прочитать файл {module.source_file}: {e}")
            return violations
        
        # 1. Проверяем процедуры
        for proc in module.procedures:
            if proc.range:
                line_before = proc.range.start.line - 1
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

        # 2. Проверяем функции
        for func in module.functions:
            if func.range:
                line_before = func.range.start.line - 1
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