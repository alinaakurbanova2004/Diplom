from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class CamelCase(BaseRule):
    """
    Правило VAR-02: Составные имена переменных должны быть в CamelCase
    Слова слитно, каждое слово начинается с большой буквы
    """

    def __init__(self):
        self.code = "VAR-02"
        self.name = "CamelCase для составных имен"
        self.description = "Имена переменных должны быть в CamelCase: слова слитно, каждое с большой буквы."
        self.severity = "WARNING"

        # Разрешённые исключения (односимвольные переменные-счётчики)
        self.single_letter_exceptions = ['i', 'j', 'k', 'n', 'm', 'x', 'y', 'z']
        
        # Русские односимвольные исключения
        self.russian_single_letter = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 
                                       'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 
                                       'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 
                                       'ъ', 'ы', 'ь', 'э', 'ю', 'я']

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        # 1. Глобальные переменные
        for var in module.variables:
            if self._is_bad_camelcase(var.name):
                line = var.range.start.line if var.range else 0
                col = var.range.start.column if var.range else 0
                violations.append(self._create_violation(var, module, None, line, col))

        # 2. Локальные переменные в процедурах
        for proc in module.procedures:
            for var in proc.local_vars:
                if self._is_bad_camelcase(var.name):
                    line = var.range.start.line if var.range else 0
                    col = var.range.start.column if var.range else 0
                    violations.append(self._create_violation(var, module, proc.name, line, col))

        # 3. Локальные переменные в функциях
        for func in module.functions:
            for var in func.local_vars:
                if self._is_bad_camelcase(var.name):
                    line = var.range.start.line if var.range else 0
                    col = var.range.start.column if var.range else 0
                    violations.append(self._create_violation(var, module, func.name, line, col))

        return violations

    def _is_bad_camelcase(self, name: str) -> bool:
        """Проверяет, соответствует ли имя правилам CamelCase"""
        
        # ИСКЛЮЧЕНИЕ 1: Пустое имя
        if not name:
            return False
        
        # ИСКЛЮЧЕНИЕ 2: Односимвольные имена (латиница)
        if len(name) == 1 and name in self.single_letter_exceptions:
            return False
        
        # ИСКЛЮЧЕНИЕ 3: Односимвольные имена (кириллица)
        if len(name) == 1 and name in self.russian_single_letter:
            return False
        
        # ИСКЛЮЧЕНИЕ 4: Имена, начинающиеся с подчеркивания
        if name.startswith('_'):
            return False
        
        # 1. Первая буква должна быть заглавной
        first_char = name[0]
        if not first_char.isupper():
            return True
        
        # 2. Не должно быть подчеркиваний
        if '_' in name:
            return True
        
        # 3. Проверка, что не все буквы заглавные (ПЛОХОЕИМЯ)
        # Если имя длиннее 2 символов и все буквы заглавные -> нарушение
        if len(name) > 2 and name.isupper():
            return True
        
        # Это для CamelCase: ПерваяЗаглавная, остальные строчные
        if name[0].isupper():
            
            pass
        
        return False

    def _create_violation(self, var, module, context=None, line=0, col=0):
        context_info = f" в {context}" if context else ""
        return Violation(
            rule_code=self.code,
            rule_name=self.name,
            severity=self.severity,
            module_name=module.name,
            line=line,
            column=col,
            message=f"Переменная '{var.name}'{context_info} должна быть в CamelCase: слова слитно, каждое с большой буквы.",
        )