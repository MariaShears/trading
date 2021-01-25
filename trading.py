import click
import datetime
import pprint
import pandas as pd
from pandas import json_normalize

from app import migrater
from app.instruments.create_instruments import create_stock_from_cli
from app.instruments.edit_instruments import edit_stock_from_cli
from app.brokers.create_brokers import create_broker_from_cli
from app.exemption.create_exemptions import create_exemption_from_cli
from app.instruments.get import get_instruments
from app.brokers.get import get_brokers
from app.exemption.get import get_exemptions
from app.exemption import exemption_calc
from app.db import session
from app import statistics
from app.exemption.exemption_calc import *
from app.instruments import Stock
from app.instruments.get import presentable_stock
from app.controllers import earnings as earnings_controller


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
def exemption_balance():
    """Show exemption balance"""
    exemptions = get_exemptions(session)
    print(calculate_total_exemption(exemptions))
    print(calculate_running_exemption_per_broker())


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
    while click.confirm('Do you want to continue?', abort=False):
        new_exemption = create_stock_from_cli(brokers)
        session.add(new_stock)
        session.commit()


@cli.command()
def list_entries():
    """List journal entries"""
    all_entries = (session.query(Stock).all())
    all_entries_printable = {}
    for u in all_entries:
        u = json_normalize(u.__dict__)
        print(u.iloc[:, 1:])


@cli.command()
def list_last_4_earnings():
    """List earnings for a stock"""
    print(get_last_4_earnings())


@cli.command()
@click.argument('symbol')
def earnings_price_effect(symbol):
    """Show counts of cases when there was and was not a price increase after a positive earnings surprise"""
    print(earnings_controller.count_price_increase_cases_on_positive_surprise(symbol))


@cli.command()
def edit_stock_entry():
    """Edit journal entries"""
    stocks = get_instrments(session)
    edited_entry = edit_stock_from_cli(stocks)
    print(edited_entry)


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


@stats.command()
def exemption_sum():
    """Returns the total exemption sum for this year"""
    exemptions = get_exemptions(session)
    this_year_exemption_sum = calculate_total_exemption(exemptions)
    click.echo('Your total exemption sum this year is', this_year_exemption_sum) 


@stats.command()
def exemption_left():
    """Returns the exemption sum left in this year"""
    exemptions = get_exemptions(session)
    this_year_exemption_left = calculate_running_exemption(exemptions)
    click.echo('Your exemption sum left this year is', this_year_exemption_left)


def check_brokers():
    brokers = get_brokers(session)
    return len(brokers) > 0


if __name__ == '__main__':
    cli()
