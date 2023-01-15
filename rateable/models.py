"""Module containing sqlalchemy models"""
from sqlalchemy import Column, String

from persistable.models import Persistable


class Rateable(Persistable):
    """
    SqlAlchemy model
    """

    __tablename__ = "rateables"

    name = Column(String)
