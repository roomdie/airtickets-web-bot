from enum import Enum
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class PurchasedTicket(Base):
    __tablename__ = "purchased_ticket"

    index: BigInteger = Column(Integer, primary_key=True)
    user_id: BigInteger = Column(BigInteger)
    passenger_name: String = Column(String)
    flight_code: String = Column(String)
    details = Column(JSON)
