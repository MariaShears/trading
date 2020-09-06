import click
import datetime

from app import migrater
from app.instruments.create_instruments import create_stock_from_cli
from app.brokers.create_brokers import create_broker_from_cli
from app.exemption.create_exemptions import create_exemption_from_cli
from app.instruments.get import get_instrments
from app.brokers import get_brokers
from app.db import session
from app import statistics


@click.group()
def cli():
    pass


@cli.command()
def new_broker_entry():
    """Add new broker to the journal"""
    new_broker = create_broker_from_cli()
    session.add(new_broker)
    session.commit()
    while click.confirm('Do you want to continue?', abort=False):
        new_broker = create_broker_from_cli()
        session.add(new_broker)
        session.commit()


@cli.command()
def new_exemption_entry():
    """Add new exemption amount to the journal"""
    if (not check_brokers()):
        print("this command requries brokers to work please enter some with the new-broker-entry command")
        return
    brokers = get_brokers(session)
    new_exemption = create_exemption_from_cli(brokers)
    session.add(new_exemption)
    session.commit()
    while click.confirm('Do you want to continue?', abort=False):
        new_exemption = create_exemption_from_cli(brokers)
        session.add(new_exemption)
        session.commit()


@cli.command()
def new_stock_entry():
    """Add new stock record to the journal"""
    if (not check_brokers()):
        print("this command requries brokers to work please enter some with the new-broker-entry command")
        return
    brokers = get_brokers(session)
    new_stock = create_stock_from_cli(brokers)
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
    statistics.print_calculations(instruments)

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


def check_brokers():
    brokers = get_brokers(session)
    return len(brokers) > 0


if __name__ == '__main__':
    cli()
