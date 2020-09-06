from sqlalchemy import Column, Float, Integer, String, Date
from app.db import Base
from sqlalchemy.orm import relationship


def get_brokers(session):
    return session.query(Broker).all()

def presentable_broker(broker):
    return (broker.name, broker)

class Broker(Base):
    __tablename__ = 'broker'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    date = Column(Date)
    comment = Column(String)

    stocks = relationship("Stock", back_populates='broker')
    exemptions = relationship("Exemption", back_populates='broker')
