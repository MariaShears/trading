from app.cli_utils import *
from app.instruments.get import presentable_stock
from app.brokers.get import presentable_broker
from sqlalchemy import inspect


def edit_stock_from_cli(session, stocks, brokers):
    entry_to_edit = get_existing_option_form_cli(
        'ID of entry you want to edit is', list(map(presentable_stock, stocks)))

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

    list_of_new_entries = {"broker": broker, "instrument": instrument, "buy_date": buy_date.date(), "sell_date": sell_date.date(), "position_size": position_size, "comission": comission,
                           "exchange_rate": exchange_rate, "entry_price": entry_price, "target_price": target_price, "bid_price": bid_price, "atr": atr, "entry_signal": entry_signal, "exit_signal": exit_signal, "comment": comment}

    mapper = inspect(entry_to_edit)
    entry_to_edit_dict = {}
    for x in mapper.attrs:
        entry_to_edit_dict[x.key] = x.value
    for k1, v1 in entry_to_edit_dict.items():
        for k2, v2 in list_of_new_entries.items():
            if k1 == k2 and v1 != v2:
                print(f"db_entry: {k1, v1} , new_entry:{k2, v2}")
                return entry_to_edit, k1, v1, k2, v2
