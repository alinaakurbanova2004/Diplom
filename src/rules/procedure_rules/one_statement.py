from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class OneStatementPerLine(BaseRule):
    """Правило FUN-01: В одной строке должен быть только один оператор"""

    def __init__(self):
        self.code = "FUN-01"
        self.name = "Один оператор в строке"
        self.description = "Не пишите нескольких операторов в одной строке"
        self.severity = "WARNING"

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        # Получаем исходный код
        if hasattr(module, 'original_code') and module.original_code:
            source_code = module.original_code
        elif hasattr(module, 'source_file') and module.source_file:
            try:
                with open(module.source_file, "r", encoding="utf-8") as f:
                    source_code = f.read()
            except Exception:
                return violations
        else:
            return violations

        lines = source_code.split('\n')
        
        for i, line in enumerate(lines, 1):
            line_stripped = line.strip()
            
            # Пропускаем пустые строки и комментарии
            if not line_stripped or line_stripped.startswith("//"):
                continue
            
            # Находим все позиции символа ';' в строке
            semicolon_positions = [pos for pos, ch in enumerate(line) if ch == ';']
            
            # Если операторов больше одного
            if len(semicolon_positions) > 1:
                # Берём позицию ВТОРОГО оператора (индекс 1)
                # +1 потому что column в 1С начинается с 1, а не с 0
                column = semicolon_positions[1] + 1
                
                violations.append(
                    Violation(
                        rule_code=self.code,
                        rule_name=self.name,
                        severity=self.severity,
                        module_name=module.name,
                        line=i,
                        column=column,  # ← теперь правильная позиция!
                        message="Строка содержит несколько операторов. Разделите их на отдельные строки.",
                    )
                )

        return violations