import click

from app import journal, migrater
from app import risk
from app import find_stock

@click.group()
def cli():
    pass

@cli.command()
@click.option('--instrument', prompt=True,
            help='The instrument used for trade [stock|KO]'
            )
def create_entry(instrument):
    """Create a trading journal entry"""
    if instrument == 'stock':
        journal.create_journal_entry_stock()
    elif instrument == 'KO':
        journal.create_journal_entry_KO()

    else: 
        click.echo('Invalid input, Try "trading --help" for help.')


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

@cli.command()
def calculate_risk():
    """Calculates position size and stop-loss for a trade"""
    click.echo('Here are your trade parameters')
    risk.calculate_trade_parameters()

@cli.command()
def return_stock():
    """Retrieves a list of wished stocks"""
    click.echo('Here is the list of stocks')
    find_stock.get_data()

# @cli.command()
# @click.option('--journal-id')
# def list_entries(journal_id):
#     """List my a trading journal entries"""
#     journal.list_entries(journal_id)


if __name__ == '__main__':
    cli()