import os

from yoyo import read_migrations, get_backend

from app.config import c

backend = get_backend('sqlite:///{}'.format(c.db_table_name))
migrations = read_migrations('migrations')

def wipe_db():
    """Deletes the sqlite db file"""
    if os.path.exists(c.db_table_name):
        os.remove(c.db_table_name)

def apply_outstanding_migrations():
    """Apply any outstanding migrations"""
    with backend.lock():
        backend.apply_migrations(backend.to_apply(migrations))