from typing import Dict
from src.rules import naming_rules, procedure_function_rules
from .basic_rule import BaseRule


class RuleRegistry:
    _rules: Dict[str, BaseRule] = {}

    @classmethod
    def initialize(cls):
        rules = [
            # Правила именования
            naming_rules.CamelCase(),
            naming_rules.FlagVariableNames(),
            naming_rules.MeaningfulVariable(),
            naming_rules.VariableMinLength(),
            naming_rules.WithoutUnderscorePrefix(),
            # Правила для процедур/функций
            procedure_function_rules.EmptyProcedure(),
            procedure_function_rules.MissingProcedureComment(),
            procedure_function_rules.OneStatementPerLine(),
            procedure_function_rules.ProcedureLength(),
            procedure_function_rules.TooManyParameters(),
        ]

        for rule in rules:
            cls.register(rule)
