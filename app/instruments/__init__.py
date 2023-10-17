from sqlalchemy import Column, Float, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.db import Base

class Stock(Base):
    __tablename__ = 'stock'

    id = Column(Integer, primary_key=True)
    broker_id = Column(Integer, ForeignKey("broker.id"))
    instrument = Column(String)
    buy_date = Column(Date)
    sell_date = Column(Date)
    buying_sum = Column(Float)
    buying_sum_comission = Column(Float)
    exchange_rate = Column(Float)
    position_size = Column(Float)
    comission = Column(Float)
    trade_profit = Column(Float)
    tax = Column(Float)
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

    broker = relationship("Broker", back_populates='stocks')
