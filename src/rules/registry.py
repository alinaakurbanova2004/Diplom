from typing import Dict, List, Optional
from src.rules import naming_rules, procedure_rules
from .base_rule import BaseRule


class RuleRegistry:
    _rules: Dict[str, BaseRule] = {}

    @classmethod
    def register(cls, rule: BaseRule):
        """Регистрирует правило"""
        cls._rules[rule.code] = rule

    @classmethod
    def get_rule(cls, code: str) -> Optional[BaseRule]:
        """Возвращает правило по коду"""
        return cls._rules.get(code)

    @classmethod
    def get_all_rules(cls) -> List[BaseRule]:
        """Возвращает все правила"""
        return list(cls._rules.values())

    @classmethod
    def get_enabled_rules(cls) -> List[BaseRule]:
        """Возвращает только включенные правила"""
        return [r for r in cls._rules.values() if r.enabled]

    @classmethod
    def initialize(cls):
        """Инициализирует и регистрирует все правила"""
        rules = [
            # Правила именования
            naming_rules.CamelCase(),
            naming_rules.FlagVariableNames(),
            naming_rules.MeaningfulVariable(),
            naming_rules.VariableMinLength(),
            naming_rules.WithoutUnderscorePrefix(),
            # Правила для процедур/функций
            procedure_rules.EmptyProcedure(),
            procedure_rules.MissingProcedureComment(),
            procedure_rules.OneStatementPerLine(),
            procedure_rules.ProcedureLength(),
            procedure_rules.TooManyParameters(),
        ]

        for rule in rules:
            cls.register(rule)


# Автоматическая инициализация при импорте
RuleRegistry.initialize()
