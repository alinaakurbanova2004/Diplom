"""
Динамическая загрузка правил из базы данных
"""

import importlib
import importlib.util
import sys
from pathlib import Path
from typing import List, Dict, Type
from src.rules.base_rule import BaseRule
from src.database.db_manager import DatabaseConnection, RuleRepository


class RuleLoader:
    """Загружает правила из БД и создаёт экземпляры классов"""
    
    def __init__(self, db: DatabaseConnection):
        self.db = db
        self.rule_repo = RuleRepository(db)
        self.rules_base_path = Path(__file__).parent.parent / "rules"
    
    def load_all_rules(self) -> List[BaseRule]:
        """Загружает все активные правила из БД"""
        rules = []
        db_rules = self.rule_repo.get_all_active_rules()
        
        print(f"📋 Загружено правил из БД: {len(db_rules)}")
        
        for db_rule in db_rules:
            try:
                rule = self._load_rule_class(db_rule)
                if rule:
                    rules.append(rule)
            except Exception as e:
                print(f"❌ Ошибка загрузки правила {db_rule['code']}: {e}")
        
        return rules
    
    def _load_rule_class(self, db_rule: Dict) -> BaseRule:
        """Динамически загружает класс правила из файла"""
        file_path = db_rule.get('file_path')
        class_name = db_rule.get('class_name')
        
        if not file_path or not class_name:
            print(f"⚠️ У правила {db_rule['code']} не указаны file_path или class_name")
            return None
        
        # Полный путь к файлу
        full_path = self.rules_base_path / file_path
        
        if not full_path.exists():
            print(f"⚠️ Файл {full_path} не найден для правила {db_rule['code']}")
            return None
        
        # Динамический импорт
        spec = importlib.util.spec_from_file_location(class_name, full_path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[class_name] = module
        spec.loader.exec_module(module)
        
        # Получаем класс
        rule_class = getattr(module, class_name, None)
        if not rule_class:
            print(f"⚠️ Класс {class_name} не найден в {full_path}")
            return None
        
        # Создаём экземпляр
        rule = rule_class()
        
        # Устанавливаем свойства из БД
        rule.id = db_rule['id']
        rule.code = db_rule['code']
        rule.name = db_rule['name']
        rule.description = db_rule['description']
        rule.severity = db_rule['severity']
        rule.enabled = db_rule['is_active']
        
        # Загружаем параметры для правила
        params = self.rule_repo.get_parameters_for_rule(db_rule['id'])
        for param in params:
            self._set_rule_param(rule, param)
        
        # Загружаем регулярные выражения для правила
        regexps = self.rule_repo.get_regexps_for_rule(db_rule['id'])
        if regexps:
            setattr(rule, 'regexps', regexps)
        
        return rule
    
    def _set_rule_param(self, rule: BaseRule, param: Dict):
        """Устанавливает параметр правила"""
        param_name = param['param_name']
        param_value = param['param_value']
        param_type = param['param_type']
        
        # Преобразуем значение в нужный тип
        if param_type == 'integer':
            param_value = int(param_value)
        elif param_type == 'boolean':
            param_value = param_value.lower() == 'true'
        
        setattr(rule, param_name, param_value)