import yaml

class __Config:
    def __init__(self):
        self._global_config = self._load_yaml()

    def _load_yaml(self):
        return yaml.safe_load(open("config.yml"))

    @property
    def db_name(self):
        return self._global_config.get('database', {}).get('file', 'default.sqlite')
    
c = __Config()