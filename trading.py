import click
import journal
import migrater

@click.group()
def cli():
    pass

@cli.command()
def create_entry():
    """Create a trading journal entry"""
    click.echo('Here is your journal summery')
    journal.create_journal_entry()

@cli.group()
def migrate():
    """Commands for database matiance"""
    pass

@migrate.command()
def apply():
    """Apply outstanding database migrations"""
    click.echo('Applying outstanding database migrations')
    migrater.apply_outstanding_migrations()

@migrate.command()
def wipe():
    """Wipe database file"""
    migrater.wipe_db()


# @cli.command()
# @click.option('--journal-id')
# def list_entries(journal_id):
#     """List my a trading journal entries"""
#     journal.list_entries(journal_id)


if __name__ == '__main__':
    cli()