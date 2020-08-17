import click
import datetime

from app import migrater
from app.instruments.create import create_stock_from_cli
from app.instruments.get import get_instrments
from app.db import session
from app import statistics

@click.group()
def cli():
    pass

@cli.command()
def new_stock_entry():
    new_stock = create_stock_from_cli()
    session.add(new_stock)
    session.commit()


@cli.group()
def migrate():
    """Commands for database maintenance"""
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

@cli.group()
def stats():
    """Commands for getting stats about trading performance"""
    pass

@stats.command()
def sum():
    """Return sum of trade profits by period"""
    instruments = get_instrments(session)
    profit = statistics.calculate_profit(instruments)
    profit_year = statistics.calculate_profit_year(instruments)
    profit_month = statistics.calculate_profit_month(instruments)
    print(f"Your overall profit is: {profit}")
    print(f"Your profit this year is: {profit_year}")
    print(f"Your profit this month is: {profit_month}")


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