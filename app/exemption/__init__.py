from sqlalchemy import Column, Float, Integer, String, Date, ForeignKey
from app.db import Base
from sqlalchemy.orm import relationship


class Exemption(Base):
    __tablename__ = 'exemption'

    id = Column(Integer, primary_key=True)
    broker_id = Column(Integer, ForeignKey("broker.id"))
    exemption_amount = Column(Float)
    date = Column(Date)
    comment = Column(String)

    broker = relationship("Broker", back_populates='exemptions')
