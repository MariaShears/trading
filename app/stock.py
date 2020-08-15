from sqlalchemy import Column, Float, Integer, String, Date
from .db import Base, _engine

class Stock(Base):
    __tablename__ = 'stocks'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    entry_signal = Column(String)
    exit_signal = Column(String)
    comment = Column(String)
    buying_sum = Column(Float)
    buying_date = Column(Date)


    def __repr__(self):
       return f"<Stock name='{self.name}'>"

# buy_date
# sell_date
# buying_sum
# buying_sum_comission
# position_size
# comission
# exchange_rate
# trade_profit
# risk_reward_ratio
# entry_price
# target_price
# bid_price
# atr
# initial_stop
# risk_per_stock