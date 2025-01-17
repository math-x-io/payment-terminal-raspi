from sqlalchemy import Column, Integer, String
from sqlalchemy.sql.sqltypes import Date, DateTime
from sqlalchemy_serializer import SerializerMixin
from database.database import Base
from datetime import datetime
from .public_data_filter import PublicDataFilter


class Scan(Base, SerializerMixin, PublicDataFilter):
    __tablename__ = 'scans'
    id = Column(Integer, primary_key=True)
    date = Column(DateTime, unique=False, default=datetime.now)
    card_uid = Column(String, unique=False)
    currency_amount = Column(Integer, unique=False)
    transaction_status = Column(String, unique=False)

    def __init__(self, card_uid, currency_amount, transaction_status):
        self.card_uid = card_uid
        self.currency_amount = currency_amount
        self.transaction_status = transaction_status
