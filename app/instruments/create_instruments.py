import datetime
from . import Stock
from app.cli_utils import *
from app.brokers.get import presentable_broker


def _caculate_initial_stop(entry_price, atr):
    return entry_price - (atr * 2)


def _caculate_risk_per_stock(entry_price, initial_stop):
    return entry_price - initial_stop


def _caculate_risk_reward_ratio(risk_per_stock, target_price, entry_price):
    try:
        return round(risk_per_stock / (target_price - entry_price), 4)
    except ZeroDivisionError:
        return 0


def _caculate_buying_sum(position_size, entry_price):
    return position_size * entry_price


def _caculate_buying_sum_comission(position_size, entry_price, comission):
    return (position_size * entry_price) + comission


def _caculate_trade_profit(exchange_rate, position_size, bid_price, entry_price, comission):
    try:
        return round((position_size * ((bid_price - entry_price)/exchange_rate) - comission), 4)
    except ZeroDivisionError:
        return (position_size * (bid_price - entry_price) - comission)

def _calculate_tax(trade_profit):
    if trade_profit > 0:
        withholding_tax = trade_profit * 0.25 
        return withholding_tax + withholding_tax * 0.055 
    else:
        return 0 

def create_stock_from_cli(brokers):
    broker = get_existing_option_form_cli(
        'Broker used for trade is', list(map(presentable_broker, brokers)))
    instrument = get_required_string_from_cli('The product ISIN/WKN is')
    buy_date = get_date_from_cli("Buy date")
    sell_date = get_date_from_cli("Sell date")
    position_size = get_required_number_from_cli('Position size of the trade')
    comission = get_number_from_cli('Overall comission charged by broker')
    exchange_rate = get_number_from_cli('Excahge rate used by broker')
    entry_price = get_required_number_from_cli("Your product's entry price")
    target_price = get_number_from_cli('Target price of the product')
    bid_price = get_required_number_from_cli('Bid price of the product')
    atr = get_number_from_cli('ATR of the product at entry time')
    entry_signal = get_optional_string_from_cli('Signal for trade entry')
    exit_signal = get_optional_string_from_cli('Signal for trade exit')
    comment = get_optional_string_from_cli(
        'Comment on the success/failure of the trade')

    # computed fields
    initial_stop = _caculate_initial_stop(entry_price, atr)
    risk_per_stock = _caculate_risk_per_stock(entry_price, initial_stop)
    risk_reward_ratio = _caculate_risk_reward_ratio(
        risk_per_stock, target_price, entry_price)
    buying_sum = _caculate_buying_sum(position_size, entry_price)
    buying_sum_comission = _caculate_buying_sum_comission(
        position_size, entry_price, comission)
    trade_profit = _caculate_trade_profit(
        exchange_rate=exchange_rate,
        position_size=position_size,
        bid_price=bid_price,
        entry_price=entry_price,
        comission=comission
    )
    tax = _calculate_tax(trade_profit)

    new_stock = Stock(
        broker=broker,
        instrument=instrument,
        buy_date=buy_date,
        sell_date=sell_date,
        buying_sum=buying_sum,
        buying_sum_comission=buying_sum_comission,
        exchange_rate=exchange_rate,
        position_size=position_size,
        comission=comission,
        trade_profit=trade_profit,
        tax=tax,
        risk_reward_ratio=risk_reward_ratio,
        entry_price=entry_price,
        target_price=target_price,
        bid_price=bid_price,
        atr=atr,
        initial_stop=initial_stop,
        risk_per_stock=risk_per_stock,
        entry_signal=entry_signal,
        exit_signal=exit_signal,
        comment=comment,
    )
    return new_stock


def create_ko_from_cli():
    """Read from prompt data needed to create a knockout"""
    new_stock = create_stock_from_cli()

    # ko only fields
    subscription_ratio = get_number_from_cli(
        'Subscription ratio of the instrument, if relevant')
    knock_out = get_number_from_cli(
        'Knock-out threshold of the instrument, if relevant')
    multiplicator = get_number_from_cli(
        'Multiplicator of the instrument, if relevant')
    strike_price = get_number_from_cli(
        'Strike price of the instrument, if relevant')
    entry_underlying_price = get_number_from_cli(
        'Underlying price at entry, if relevant')
