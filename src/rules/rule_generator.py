"""
Генератор файлов правил анализа на основе параметров из БД
"""

import os
from pathlib import Path
from typing import Dict, Any, Optional


class RuleGenerator:
    """Генерирует и обновляет Python-файлы правил анализа"""
    
    RULES_DIR = Path(__file__).parent  # src/rules/
    
    @classmethod
    def generate_rule_file_by_id(cls, rule_id: int, db_connection) -> str:
        """Генерирует файл правила по ID из БД"""
        from src.database.db_manager import RuleRepository
        
        rule_repo = RuleRepository(db_connection)
        rule_data = rule_repo.get_rule_by_id(rule_id)
        params = rule_repo.get_parameters_for_rule(rule_id)
        
        param_dict = {p['param_name']: p['param_value'] for p in params}
        rule_type = cls._detect_rule_type(rule_data['code'], param_dict)
        
        full_data = {
            'id': rule_data['id'],
            'code': rule_data['code'],
            'name': rule_data['name'],
            'description': rule_data.get('description', ''),
            'severity': rule_data['severity'],
            'rule_type': rule_type,
            **param_dict
        }
        
        return cls._generate_rule_file_from_data(full_data)
    
    @classmethod
    def generate_new_rule(cls, form_data: Dict[str, Any], db_connection) -> int:
        """Создаёт новое правило: запись в БД + файл"""
        from src.database.db_manager import RuleRepository
        
        rule_repo = RuleRepository(db_connection)
        
        # Определяем тип правила
        rule_type = cls._detect_rule_type(form_data.get('code', ''), form_data)
        
        # Формируем имя класса и файла
        code = form_data['code']
        class_name = cls._generate_class_name(code)
        filename = cls._generate_filename(code)
        
        # Сохраняем в БД
        rule_data = {
            'code': code,
            'name': form_data['name'],
            'description': form_data.get('description', ''),
            'severity': form_data.get('severity', 'WARNING'),
            'is_active': form_data.get('is_active', True),
            'file_path': filename,
            'class_name': class_name
        }
        rule_id = rule_repo.save_rule(rule_data)
        
        # Сохраняем параметры
        cls._save_parameters(rule_id, form_data, rule_repo)
        
        # Генерируем файл
        full_data = {
            'id': rule_id,
            'code': code,
            'name': form_data['name'],
            'description': form_data.get('description', ''),
            'severity': form_data.get('severity', 'WARNING'),
            'rule_type': rule_type,
            **form_data
        }
        cls._generate_rule_file_from_data(full_data)
        
        return rule_id
    
    @classmethod
    def update_rule(cls, rule_id: int, form_data: Dict[str, Any], db_connection) -> bool:
        """Обновляет существующее правило: БД + файл"""
        from src.database.db_manager import RuleRepository
        
        rule_repo = RuleRepository(db_connection)
        
        # 1. Обновляем основную информацию
        rule_repo.update_rule(rule_id, {
            'name': form_data.get('name'),
            'description': form_data.get('description', ''),
            'severity': form_data.get('severity', 'WARNING'),
            'is_active': form_data.get('is_active', True)
        })
        
        # 2. Обновляем параметры
        rule_repo.delete_rule_parameters(rule_id)
        cls._save_parameters(rule_id, form_data, rule_repo)
        
        # 3. Перегенерируем файл
        cls.generate_rule_file_by_id(rule_id, db_connection)
        
        return True
    
    @classmethod
    def delete_rule(cls, rule_id: int, db_connection) -> bool:
        """Удаляет правило: БД + файл"""
        from src.database.db_manager import RuleRepository
        
        rule_repo = RuleRepository(db_connection)
        rule_data = rule_repo.get_rule_by_id(rule_id)
        
        if not rule_data:
            return False
        
        # Удаляем файл
        file_path = cls.RULES_DIR / rule_data.get('file_path', '')
        if file_path.exists():
            file_path.unlink()
        
        # Удаляем из БД
        return rule_repo.delete_rule(rule_id)
    
    # ==================== ВСПОМОГАТЕЛЬНЫЕ МЕТОДЫ ====================
    
    @classmethod
    def _detect_rule_type(cls, code: str, params: Dict[str, Any]) -> str:
        if code.startswith('FUN') and ('max_params' in params or params.get('max_params')):
            return 'max_params'
        if 'min_length' in params:
            return 'min_length'
        if 'forbidden_words' in params:
            return 'forbidden_words'
        if 'camelcase_prefix' in params:
            return 'camelcase'
        return 'custom'
    
    @classmethod
    def _save_parameters(cls, rule_id: int, data: Dict[str, Any], rule_repo) -> None:
        param_mapping = {
            'max_params': ('integer', int),
            'min_length': ('integer', int),
            'forbidden_words': ('string', str),
            'camelcase_prefix': ('string', str),
        }
        for param_name, (param_type, converter) in param_mapping.items():
            if param_name in data and data[param_name]:
                value = data[param_name]
                if converter == int:
                    value = int(value)
                rule_repo.save_rule_parameter(rule_id, param_name, str(value), param_type)
    
    @classmethod
    def _generate_class_name(cls, code: str) -> str:
        parts = code.replace('-', '_').split('_')
        return ''.join(word.capitalize() for word in parts)
    
    @classmethod
    def _generate_filename(cls, code: str) -> str:
        return f"{code.lower().replace('-', '_')}.py"
    
    @classmethod
    def _generate_rule_file_from_data(cls, data: Dict[str, Any]) -> str:
        """Генерирует файл правила на основе данных"""
        code = data['code']
        class_name = cls._generate_class_name(code)
        filename = cls._generate_filename(code)
        
        filepath = cls.RULES_DIR / filename
        rule_type = data.get('rule_type', 'custom')
        
        if rule_type == 'max_params':
            content = cls._generate_max_params_rule(data, class_name)
        elif rule_type == 'min_length':
            content = cls._generate_min_length_rule(data, class_name)
        elif rule_type == 'forbidden_words':
            content = cls._generate_forbidden_words_rule(data, class_name)
        elif rule_type == 'camelcase':
            content = cls._generate_camelcase_rule(data, class_name)
        else:
            content = cls._generate_custom_rule(data, class_name)
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        
        return str(filepath)
    
    # ==================== ГЕНЕРАТОРЫ КОДА ДЛЯ РАЗНЫХ ТИПОВ ПРАВИЛ ====================
    
    @classmethod
    def _generate_max_params_rule(cls, data: Dict, class_name: str) -> str:
        max_params = data.get('max_params', 8)
        severity = data.get('severity', 'WARNING')
        code = data['code']
        name = data['name']
        description = data.get('description', f'Максимум {max_params} параметров')
        
        return f'''"""
Правило {code}: {name}
Сгенерировано автоматически. Максимум параметров: {max_params}
"""

from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class {class_name}(BaseRule):
    def __init__(self):
        self.code = "{code}"
        self.name = "{name}"
        self.description = "{description}"
        self.severity = "{severity}"
        self.max_params = {max_params}
    
    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        for func in module.functions:
            if len(func.parameters) > self.max_params:
                line = func.range.start.line if func.range else 0
                violations.append(Violation(
                    rule_code=self.code, rule_name=self.name,
                    severity=self.severity, module_name=module.name,
                    line=line, column=0,
                    message=f"Функция '{{func.name}}' имеет {{len(func.parameters)}} параметров (макс. {self.max_params})"
                ))
        for proc in module.procedures:
            if len(proc.parameters) > self.max_params:
                line = proc.range.start.line if proc.range else 0
                violations.append(Violation(
                    rule_code=self.code, rule_name=self.name,
                    severity=self.severity, module_name=module.name,
                    line=line, column=0,
                    message=f"Процедура '{{proc.name}}' имеет {{len(proc.parameters)}} параметров (макс. {self.max_params})"
                ))
        return violations
'''
    
    @classmethod
    def _generate_min_length_rule(cls, data: Dict, class_name: str) -> str:
        min_length = data.get('min_length', 3)
        severity = data.get('severity', 'WARNING')
        code = data['code']
        name = data['name']
        
        return f'''"""
Правило {code}: {name}
Сгенерировано автоматически. Минимальная длина: {min_length}
"""

from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class {class_name}(BaseRule):
    def __init__(self):
        self.code = "{code}"
        self.name = "{name}"
        self.severity = "{severity}"
        self.min_length = {min_length}
        self.loop_counters = ["i", "j", "k", "n", "m", "x", "y", "z"]
    
    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        for var in module.variables:
            if len(var.name) < self.min_length and var.name not in self.loop_counters:
                line = var.range.start.line if var.range else 0
                violations.append(Violation(
                    rule_code=self.code, rule_name=self.name,
                    severity=self.severity, module_name=module.name,
                    line=line, column=0,
                    message=f"Переменная '{{var.name}}' слишком короткая (мин. {self.min_length})"
                ))
        for proc in module.procedures:
            for var in proc.local_vars:
                if len(var.name) < self.min_length and var.name not in self.loop_counters:
                    line = var.range.start.line if var.range else 0
                    violations.append(Violation(
                        rule_code=self.code, rule_name=self.name,
                        severity=self.severity, module_name=module.name,
                        line=line, column=0,
                        message=f"Переменная '{{var.name}}' в '{{proc.name}}' слишком короткая (мин. {self.min_length})"
                    ))
        return violations
'''
    
    @classmethod
    def _generate_forbidden_words_rule(cls, data: Dict, class_name: str) -> str:
        forbidden_words = data.get('forbidden_words', '')
        forbidden_list = [w.strip() for w in forbidden_words.split(',')]
        severity = data.get('severity', 'WARNING')
        code = data['code']
        name = data['name']
        
        return f'''"""
Правило {code}: {name}
Сгенерировано автоматически. Запрещённые слова: {forbidden_words}
"""

from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class {class_name}(BaseRule):
    def __init__(self):
        self.code = "{code}"
        self.name = "{name}"
        self.severity = "{severity}"
        self.forbidden_words = {forbidden_list}
    
    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        for var in module.variables:
            if var.name.lower() in self.forbidden_words:
                line = var.range.start.line if var.range else 0
                violations.append(Violation(
                    rule_code=self.code, rule_name=self.name,
                    severity=self.severity, module_name=module.name,
                    line=line, column=0,
                    message=f"Переменная '{{var.name}}' использует запрещённое слово"
                ))
        return violations
'''
    
    @classmethod
    def _generate_camelcase_rule(cls, data: Dict, class_name: str) -> str:
        prefix = data.get('camelcase_prefix', '')
        severity = data.get('severity', 'WARNING')
        code = data['code']
        name = data['name']
        
        return f'''"""
Правило {code}: {name}
Сгенерировано автоматически. Префикс: {prefix}
"""

from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class {class_name}(BaseRule):
    def __init__(self):
        self.code = "{code}"
        self.name = "{name}"
        self.severity = "{severity}"
        self.prefix = "{prefix}"
    
    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        for var in module.variables:
            if self.prefix and not var.name.startswith(self.prefix):
                line = var.range.start.line if var.range else 0
                violations.append(Violation(
                    rule_code=self.code, rule_name=self.name,
                    severity=self.severity, module_name=module.name,
                    line=line, column=0,
                    message=f"Переменная '{{var.name}}' должна начинаться с '{{self.prefix}}'"
                ))
        return violations
'''
    
    @classmethod
    def _generate_custom_rule(cls, data: Dict, class_name: str) -> str:
        code = data['code']
        name = data['name']
        severity = data.get('severity', 'WARNING')
        
        return f'''"""
Правило {code}: {name}
Сгенерировано автоматически. Требуется ручная доработка логики.
"""

from typing import List
from src.parser.ast_nodes import ModuleNode
from src.rules.base_rule import BaseRule
from src.rules.violation import Violation


class {class_name}(BaseRule):
    def __init__(self):
        self.code = "{code}"
        self.name = "{name}"
        self.severity = "{severity}"
    
    def check(self, module: ModuleNode) -> List[Violation]:
        violations = []
        # TODO: Реализовать логику проверки
        return violations
'''