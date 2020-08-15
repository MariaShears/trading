import datetime
from sqlalchemy import Column, Float, Integer, String, Date
from .db import Base, _engine

def get_number_from_cli(description):
    """Gets a number from the command line defaulting to 0"""
    num = None
    while num is None:
        try:
            num = float(input(f"{description}: ") or 0)
        except Exception:
            print(f"{description} should be a number")
    return num

def create_stock_from_cli():
    instrument = input("The product ISIN/WKN is: ") or "n/a"
    buy_date = input("Date trade entered ex[01.01.1993]: " ) or "n/a"
    sell_date = input("Date trade closed ex[01.01.1993]: " ) or "n/a"
    position_size = get_number_from_cli('Position size of the trade')
    comission = get_number_from_cli('Overall comission charged by broker')
    exchange_rate = get_number_from_cli('Excahge rate used by broker')
    entry_price = get_number_from_cli("Your product's entry price")
    target_price = get_number_from_cli('Target price of the product')
    bid_price = get_number_from_cli('Bid price of the product')
    atr = get_number_from_cli('ATR of the product at entry time')
    entry_signal = input("Signal for trade entry: ") or "n/a"
    exit_signal = input("Signal for trade exit: ") or "n/a"
    comment = input("Comment on the success/failure of the trade: ") or "n/a"

    initial_stop = (entry_price) - (atr * 2)

    # calculate risk per stock
    risk_per_stock = entry_price - initial_stop

    # calculate risk/reward ratio
    risk_reward_ratio = None
    if risk_reward_ratio is None:
        try:
            risk_reward_ratio = risk_per_stock/(target_price - entry_price)
        except ZeroDivisionError:
            risk_reward_ratio = 0

    # calculate buying sum
    buying_sum = position_size * entry_price

    # calculate buying sum with comission
    buying_sum_comission = (position_size * entry_price) + comission

    # calculate profit of trade
    if exchange_rate == 0:
        trade_profit = (position_size * (bid_price - entry_price) - comission)
    else:
        trade_profit = (position_size * ((bid_price - entry_price)/exchange_rate) - comission)

    new_stock = Stock(
        instrument = instrument,
        buy_date = datetime.datetime.strptime(buy_date, '%d.%m.%Y'),
        sell_date = datetime.datetime.strptime(sell_date, '%d.%m.%Y'),
        buying_sum = buying_sum,
        buying_sum_comission = buying_sum_comission,
        exchange_rate = exchange_rate,
        position_size = position_size,
        comission = comission,
        trade_profit = trade_profit,
        risk_reward_ratio = risk_reward_ratio,
        entry_price = entry_price,
        target_price = target_price,
        bid_price = bid_price,
        atr = atr,
        initial_stop = initial_stop,
        risk_per_stock = risk_per_stock,
        entry_signal = entry_signal,
        exit_signal = exit_signal,
        comment = comment,
    )
    return new_stock


class Stock(Base):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True)
    instrument = Column(String)
    buy_date = Column(Date)
    sell_date = Column(Date)
    buying_sum = Column(Float)
    buying_sum_comission = Column(Float)
    exchange_rate = Column(Float)
    position_size = Column(Float)
    comission = Column(Float)
    trade_profit = Column(Float)
    risk_reward_ratio = Column(Float)
    entry_price = Column(Float)
    target_price = Column(Float)
    bid_price = Column(Float)
    atr = Column(Float)
    initial_stop = Column(Float)
    risk_per_stock = Column(Float)
    entry_signal = Column(String)
    exit_signal = Column(String)
    comment = Column(String)

    # def __repr__(self):
    #    return f"<Stock name='{self.name}'>"