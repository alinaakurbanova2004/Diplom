from typing import List
from src.parser.ast_nodes import ModuleNode, ProcedureNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class DocumentMovementOrder(BaseRule):
    """
    Правило FUN-20: Порядок записи движений документа

    Проверяет, что в обработчике ПередЗаписью документа:
    1. Установка движений (УстановитьДвижения) выполняется
    2. Это происходит после заполнения всех реквизитов
    """

    def __init__(self):
        self.code = "FUN-20"
        self.name = "Порядок записи движений документа"
        self.description = (
            "Запись движений документа должна выполняться в обработчике ПередЗаписью "
            "после установки всех реквизитов и перед началом транзакций с регистрами."
        )
        self.severity = "WARNING"

    def _find_before_write_handler(self, module: ModuleNode):
        """Находит процедуру ПередЗаписью в модуле документа"""
        for proc in module.procedures:
            if proc.name == "ПередЗаписью":
                return proc
        return None

    def _has_movement_operations(self, body: list) -> bool:
        """Проверяет, есть ли в теле операции с движениями"""
        for node in body:
            # Проверяем исходный код строки
            if hasattr(node, 'text') and node.text:
                if 'УстановитьДвижения' in node.text or 'Движения' in node.text:
                    return True
            # Рекурсивный обход вложенных конструкций
            if hasattr(node, 'body') and isinstance(node.body, list):
                if self._has_movement_operations(node.body):
                    return True
        return False

    def _find_record_operation(self, body: list) -> tuple:
        """Находит операцию записи движения и её позицию"""
        for i, node in enumerate(body):
            if hasattr(node, 'text') and node.text:
                if 'УстановитьДвижения' in node.text:
                    return True, i
            if hasattr(node, 'body') and isinstance(node.body, list):
                found, pos = self._find_record_operation(node.body)
                if found:
                    return True, pos
        return False, -1

    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []

        # Проверяем, что модуль является документом
        if hasattr(module, 'name') and module.name:
            if not ('Документ' in module.name or 'Document' in module.name):
                return violations

        # Находим обработчик ПередЗаписью
        before_write = self._find_before_write_handler(module)
        if not before_write:
            return violations

        # Проверяем, есть ли операции с движениями
        if not self._has_movement_operations(before_write.body):
            line = before_write.range.start.line if before_write.range else 0
            violations.append(Violation(
                rule_code=self.code,
                rule_name=self.name,
                severity=self.severity,
                module_name=module.name,
                line=line,
                column=0,
                message="В обработчике ПередЗаписью отсутствует установка движений документа."
            ))
            return violations

        # Проверяем, что установка движений не в начале (должны быть заполнены реквизиты)
        has_record, record_pos = self._find_record_operation(before_write.body)
        
        if has_record and record_pos == 0:
            # Установка движений в первой строке — плохо!
            line = before_write.range.start.line if before_write.range else 0
            violations.append(Violation(
                rule_code=self.code,
                rule_name=self.name,
                severity=self.severity,
                module_name=module.name,
                line=line,
                column=0,
                message="Установка движений должна выполняться после заполнения всех реквизитов документа."
            ))

        return violations