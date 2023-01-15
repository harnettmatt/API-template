"""Module containing sqlalchemy models"""
from sqlalchemy import Column, String

from persistable.models import Persistable


class User(Persistable):
    """
    SqlAlchemy model
    """

    __tablename__ = "users"

    first_name = Column(String)
    last_name = Column(String)
