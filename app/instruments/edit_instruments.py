import logging
import click

from sqlalchemy import inspect

from app.cli_utils import *
from app.instruments.get import presentable_stock
from app.brokers.get import presentable_broker

logger = logging.getLogger()
logger.setLevel(logging.INFO)


def edit_stock_from_cli(session, stocks, brokers):
    entry_to_edit = get_existing_option_form_cli(
        'ID of entry you want to edit is', list(map(presentable_stock, stocks)))

    broker = get_existing_option_form_cli(
        'Broker used for trade is', list(map(presentable_broker, brokers)), entry_to_edit.broker_id)
    instrument = get_required_string_from_cli(
        'The product ISIN/WKN is', entry_to_edit.instrument)
    buy_date = get_date_from_cli("Buy date", datetime.datetime.strftime(
        entry_to_edit.buy_date, '%d.%m.%Y'))
    sell_date = get_date_from_cli("Sell date", datetime.datetime.strftime(
        entry_to_edit.sell_date, '%d.%m.%Y'))
    position_size = get_required_number_from_cli(
        'Position size of the trade', str(entry_to_edit.position_size))
    comission = get_number_from_cli(
        'Overall comission charged by broker', str(entry_to_edit.comission))
    exchange_rate = get_number_from_cli(
        'Excahge rate used by broker', str(entry_to_edit.exchange_rate))
    entry_price = get_required_number_from_cli(
        "Your product's entry price", str(entry_to_edit.entry_price))
    target_price = get_number_from_cli(
        'Target price of the product', str(entry_to_edit.target_price))
    bid_price = get_required_number_from_cli(
        'Bid price of the product', str(entry_to_edit.bid_price))
    atr = get_number_from_cli(
        'ATR of the product at entry time', str(entry_to_edit.atr))
    entry_signal = get_optional_string_from_cli(
        'Signal for trade entry', entry_to_edit.entry_signal)
    exit_signal = get_optional_string_from_cli(
        'Signal for trade exit', entry_to_edit.exit_signal)
    comment = get_optional_string_from_cli(
        'Comment on the success/failure of the trade', entry_to_edit.comment)

    list_of_new_entries = {"broker": broker, "instrument": instrument, "buy_date": buy_date.date(), "sell_date": sell_date.date(), "position_size": position_size, "comission": comission,
                           "exchange_rate": exchange_rate, "entry_price": entry_price, "target_price": target_price, "bid_price": bid_price, "atr": atr, "entry_signal": entry_signal, "exit_signal": exit_signal, "comment": comment}

    mapper = inspect(entry_to_edit)
    entry_to_edit_dict = {}
    for x in mapper.attrs:
        entry_to_edit_dict[x.key] = x.value
    changed_entries_dict = {}
    for attribute, value in entry_to_edit_dict.items():
        for new_attribute, new_value in list_of_new_entries.items():
            if attribute == new_attribute and value != new_value:
                data = {attribute: new_value}
                for key, val in data.items():
                    changed_entries_dict[key] = val
                logging.info("Change in the following entries detected:")
                logging.info(f"existing_fields: {attribute, value}, changed_fields:{new_attribute, new_value}")
                if click.confirm('do you want to update?', abort=False):
                    setattr(entry_to_edit, attribute, new_value)
                    session.commit()
                    logging.info('Entry has been updated!')
    if not changed_entries_dict:
        logging.info("No changes detected!")