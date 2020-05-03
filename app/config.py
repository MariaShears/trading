import pprint
import yaml

class __Config:
    def __init__(self):
        self._global_config = self._load_yaml()

    def _load_yaml(self):
        return yaml.safe_load(open("config.yml"))

    @property
    def db_table_name(self):
        return self._global_config.get('db_name', 'default.sqlite')
    
c = __Config()