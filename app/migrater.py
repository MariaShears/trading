import os

from app.config import c

def wipe_db():
    """Deletes the sqlite db file"""
    if os.path.exists(c.db_name):
        os.remove(c.db_name)