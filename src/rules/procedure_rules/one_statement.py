from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class OneStatementPerLine(BaseRule):
    """Правило FUN-01: В одной строке должен быть только один оператор"""

    def __init__(self):
        self.code = "FUN-01"
        self.name = "Один оператор в строке"
        self.description = "Не пишите несколько операторов в одной строке"
        self.severity = "WARNING"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        # Проверяем наличие файла
        if not hasattr(module, 'source_file') or not module.source_file:
            print("⚠️ Нет информации о файле для правила FUN-01")
            return violations

        # Читаем файл
        try:
            with open(module.source_file, "r", encoding="utf-8") as f:
                lines = f.readlines()
        except Exception as e:
            print(f"⚠️ Не удалось прочитать файл {module.source_file}: {e}")
            return violations

        # Анализируем исходный код по строкам
        for i, line in enumerate(lines, 1):
            line = line.strip()
            # Пропускаем пустые строки и строки с комментариями (опционально)
            if not line or line.startswith("//"):
                continue
            
            if line.count(";") > 1:
                violations.append(
                    Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=i,
                        column=1,
                        message="Строка содержит несколько операторов. Разделите их на отдельные строки.",
                    )
                )

        return violations