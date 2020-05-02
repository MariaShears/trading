from yoyo import read_migrations, get_backend
import config

backend = get_backend('sqlite:///{}'.format(config.global_config['db_name']))
migrations = read_migrations('migrations')

def apply_outstanding_migrations():
    with backend.lock():
        # Apply any outstanding migrations
        backend.apply_migrations(backend.to_apply(migrations))