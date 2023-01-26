"""Module containing sqlalchemy models"""
from sqlalchemy import Column, String

from persistable.models import Persistable


class Item(Persistable):
    """
    SqlAlchemy model
    """

    __tablename__ = "items"

    name = Column(String)
