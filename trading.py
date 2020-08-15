import click
import datetime

from app import migrater
from app.stock import Stock
from app.db import session

@click.group()
def cli():
    pass

@cli.command()
@click.option('--name', prompt=True, type=str, required=True)
@click.option('--buying_sum', prompt=True, type=float, required=True)
@click.option('--buying_date', prompt="Buying Date ex:[01.01.1993]", type=str, required=True)
@click.option('--entry_signal', prompt=True, type=str, required=True)
@click.option('--exit_signal', prompt=True, type=str, required=True)
@click.option('--comment', prompt=True, type=str)
def new_stock_entry(name, buying_sum, buying_date, entry_signal, exit_signal, comment):
    new_stock = Stock(
        name = name,
        buying_sum = buying_sum,
        entry_signal = entry_signal,
        exit_signal = exit_signal,
        buying_date = datetime.datetime.strptime(buying_date, '%d.%m.%Y'),
        comment = comment
    )
    session.add(new_stock)
    session.commit()


@cli.group()
def migrate():
    """Commands for database matiance"""
    pass

@migrate.command()
def wipe():
    """Wipe database file"""
    migrater.wipe_db()

# @cli.command()
# def calculate_risk():
#     """Calculates position size and stop-loss for a trade"""
#     click.echo('Here are your trade parameters')
#     risk.calculate_trade_parameters()

# @cli.command()
# def return_stock():
#     """Retrieves a list of wished stocks"""
#     click.echo('Here is the list of stocks')
#     find_stock.get_data()

# @cli.command()
# @click.option('--journal-id')
# def list_entries(journal_id):
#     """List my a trading journal entries"""
#     journal.list_entries(journal_id)


if __name__ == '__main__':
    cli()