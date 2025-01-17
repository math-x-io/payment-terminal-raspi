from sqlalchemy import Column, Integer, String, Table, ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from sqlalchemy.orm import relationship
from .product import Product, UserProductAssociation
from database.database import Base
from sqlalchemy_serializer import SerializerMixin
from datetime import datetime
from .public_data_filter import PublicDataFilter


class User(Base, SerializerMixin, PublicDataFilter):
    __tablename__ = 'users'
    user_id = Column(Integer, primary_key=True, autoincrement=True)
    card_uid = Column(String, nullable=False)
    creation_date = Column(DateTime, default=datetime.now)
    update_date = Column(DateTime, default=None)
    currency_amount = Column(Integer, default=0)
    name = Column(String, default=None)
    first_name = Column(String, default=None)
    email = Column(String, default=None)
    admin = Column(Integer, default=False)
    products = relationship(UserProductAssociation)

    def __init__(self, card_uid, currency_amount):
        self.card_uid = card_uid
        self.currency_amount = currency_amount
