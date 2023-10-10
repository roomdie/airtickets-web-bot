from enum import Enum
from sqlalchemy import Column, Integer, String, DateTime, BigInteger, JSON
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Flight(Base):
    __tablename__ = "flight"

    index: BigInteger = Column(Integer, primary_key=True)
    code: String = Column(String)
    details = Column(JSON)
