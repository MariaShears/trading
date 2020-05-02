import os
from yoyo import read_migrations, get_backend
import config

backend = get_backend('sqlite:///{}'.format(config.global_config['db_name']))
migrations = read_migrations('migrations')

def wipe_db():
    """Deletes the sqlite db file"""
    if os.path.exists(config.global_config['db_name']):
        os.remove(config.global_config['db_name'])

def apply_outstanding_migrations():
    """Apply any outstanding migrations"""
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))