import datetime
import uuid
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String, Identity, ARRAY, null, JSON, UUID
from sqlalchemy.ext.declarative import (
    declared_attr)
from sqlalchemy.orm import relationship, as_declarative


@as_declarative()
class Base(object):
    @declared_attr
    def __tablename__(cls):
        """
        Sets the lowered class name as a table names with added 's'
        """
        return f'{cls.__name__.lower()}s'


class Property(Base):

    unique_id = Column(String(255), primary_key=True)
    postcode = Column(String, unique=False, nullable=True)
    paon = Column(String, unique=False, nullable=True)
    saon = Column(String, unique=False, nullable=True)
    street = Column(String, unique=False, nullable=True)
    locality = Column(String, unique=False, nullable=True)
    town_city = Column(String, unique=False, nullable=True)
    district = Column(String, unique=False, nullable=True)
    country = Column(String, unique=False, nullable=True)
    transactions = Column(String, unique=False, nullable=True)


class Transaction(Base):
    transaction_id = Column(String(255), primary_key=True)
    property_id = Column(String, unique=False, nullable=True)
    price = Column(String, unique=False, nullable=True)
    date_of_transfer = Column(String, unique=False, nullable=True)


class Postcode(Base):
    postcode = Column(String(255), primary_key=True)
    properties = Column(String, unique=False, nullable=True)
