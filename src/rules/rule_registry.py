from typing import Dict, List, Optional
from .base_rule import BaseRule


class RuleRegistry:
    """
    Реестр правил для быстрого доступа по коду.
    Правила загружаются через RuleLoader и регистрируются здесь.
    """
    
    _rules: Dict[str, BaseRule] = {}

    @classmethod
    def register(cls, rule: BaseRule):
        """Регистрирует одно правило"""
        cls._rules[rule.code] = rule

    @classmethod
    def register_many(cls, rules: List[BaseRule]):
        """Регистрирует список правил"""
        for rule in rules:
            cls._rules[rule.code] = rule

    @classmethod
    def get_rule(cls, code: str) -> Optional[BaseRule]:
        """Возвращает правило по коду (быстрый поиск)"""
        return cls._rules.get(code)

    @classmethod
    def get_all_rules(cls) -> List[BaseRule]:
        """Возвращает все зарегистрированные правила"""
        return list(cls._rules.values())

    @classmethod
    def get_enabled_rules(cls) -> List[BaseRule]:
        """Возвращает только включенные правила"""
        return [r for r in cls._rules.values() if getattr(r, 'enabled', True)]

    @classmethod
    def clear(cls):
        """Очищает реестр (полезно для тестов)"""
        cls._rules.clear()