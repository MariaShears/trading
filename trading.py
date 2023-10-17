import click

from app import migrater
from app import statistics
from app import risk
from app.db import session
from app.instruments import Stock
from app.instruments.get import get_instruments
from app.instruments.create_instruments import create_stock_from_cli
from app.instruments.edit_instruments import edit_stock_from_cli
from app.exemption.get import get_exemptions
from app.exemption.exemption_calc import *
from app.exemption.create_exemptions import create_exemption_from_cli
from app.brokers.create_brokers import create_broker_from_cli
from app.brokers.get import get_brokers
from app.controllers import earnings as earnings_controller


def check_brokers():
    brokers = get_brokers(session)
    return len(brokers) > 0


@click.group()
def cli():
    pass


@cli.command()
def new_broker_entry():
    """add new broker to the journal"""
    new_broker = create_broker_from_cli()
    session.add(new_broker)
    session.commit()
    while click.confirm('do you want to continue?', abort=False):
        new_broker = create_broker_from_cli()
        session.add(new_broker)
        session.commit()


@cli.command()
def new_exemption_entry():
    """add new exemption amount to the journal"""
    if (not check_brokers()):
        print("this command requries brokers to work please enter some with the new-broker-entry command")
        return
    brokers = get_brokers(session)
    new_exemption = create_exemption_from_cli(brokers)
    session.add(new_exemption)
    session.commit()
    while click.confirm('do you want to continue?', abort=False):
        new_exemption = create_exemption_from_cli(brokers)
        session.add(new_exemption)
        session.commit()


@cli.command()
def new_stock_entry():
    """add new stock record to the journal"""
    if (not check_brokers()):
        print("this command requries brokers to work please enter some with the new-broker-entry command")
        return
    brokers = get_brokers(session)
    new_stock = create_stock_from_cli(brokers)
    session.add(new_stock)
    session.commit()
    while click.confirm('do you want to continue?', abort=False):
        new_stock = create_stock_from_cli(brokers)
        session.add(new_stock)
        session.commit()


@cli.command()
def edit_stock_entry():
    """edit journal entries of stocks"""
    stocks = get_instruments(session)
    brokers = get_brokers(session)
    edit_stock_from_cli(session, stocks, brokers)


@cli.command()
def list_entries():
    """list journal stock entries"""
    all_entries = (session.query(Stock).all())
    print(earnings_controller.get_all_entries_df(all_entries))


@cli.command()
def exemption_balance():
    """Show exemption balance"""
    exemptions = get_exemptions(session)
    this_year_exemption_sum = calculate_total_exemption(exemptions)
    this_year_exemption_left = calculate_running_exemption(exemptions)
    print('Your total exemption sum this year is:',
          this_year_exemption_sum)
    print('Your exemption sum left this year is:',
          this_year_exemption_left)


@cli.command()
def stats():
    """Commands for getting stats about trading performance"""
    instruments = get_instruments(session)
    statistics.print_calculations(instruments)

@cli.command()
def calculate_risk():
    """Calculate risk parameters of the trade"""
    # instruments = get_instruments(session)
    risk.calculate_trade_parameters()


@cli.command()
@click.argument('symbol')
def list_last_4_earnings(symbol):
    """List earnings for a stock"""
    print(earnings_controller.get_last_4_earnings(symbol))


@cli.group()
def migrate():
    """Commands for database maintenance"""
    pass


@migrate.command()
def wipe():
    """Wipe database file"""
    migrater.wipe_db()


if __name__ == '__main__':
    cli()
