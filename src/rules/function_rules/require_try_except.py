from typing import List
from src.parser.ast_nodes import ModuleNode, TryExceptNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class RequireTryExcept(BaseRule):
    """
    Правило FUN-15: Обработка исключений
    Опасные операции должны быть обёрнуты в Попытка-Исключение.
    """

    def __init__(self):
        self.code = "FUN-15"
        self.name = "Обработка исключений"
        self.description = "Опасные операции должны быть обёрнуты в Попытка-Исключение."
        self.severity = "WARNING"
        self.dangerous_keywords = [
            "ОткрытьФайл",
            "СоздатьКаталог",
            "УдалитьФайлы",
            "КопироватьФайл",
            "ПереместитьФайл",
            "Подключить",
            "Отключить",
            "Выполнить"
        ]

    def _has_try_except_in_scope(self, body: list) -> bool:
        """Проверяет, есть ли в теле конструкция Попытка-Исключение"""
        for node in body:
            if isinstance(node, TryExceptNode):
                return True
            if hasattr(node, 'body') and isinstance(node.body, list):
                if self._has_try_except_in_scope(node.body):
                    return True
        return False

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        
        for proc in module.procedures:
            if not self._has_try_except_in_scope(proc.body):
                # Проверяем, есть ли опасные операции
                if hasattr(module, 'original_code') and module.original_code:
                    for keyword in self.dangerous_keywords:
                        if keyword in module.original_code:
                            line = proc.range.start.line if proc.range else 0
                            violations.append(Violation(
                                rule_code=self.code,
                                rule_name=self.name,
                                severity=self.severity,
                                module_name=module.name,
                                line=line,
                                column=0,
                                message=f"Процедура '{proc.name}' содержит опасные операции без обработки исключений (Попытка-Исключение)"
                            ))
                            break
        
        for func in module.functions:
            if not self._has_try_except_in_scope(func.body):
                if hasattr(module, 'original_code') and module.original_code:
                    for keyword in self.dangerous_keywords:
                        if keyword in module.original_code:
                            line = func.range.start.line if func.range else 0
                            violations.append(Violation(
                                rule_code=self.code,
                                rule_name=self.name,
                                severity=self.severity,
                                module_name=module.name,
                                line=line,
                                column=0,
                                message=f"Функция '{func.name}' содержит опасные операции без обработки исключений (Попытка-Исключение)"
                            ))
                            break
        
        return violations