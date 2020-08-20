from sqlalchemy import Column, Float, Integer, String, Date
from app.db import Base

class Broker(Base):
    __tablename__ = 'brokers'

    id = Column(Integer, primary_key=True)
    broker = Column(String)
    date = Column(Date)
    tax_exemption = Column(Float)
    comment = Column(String)