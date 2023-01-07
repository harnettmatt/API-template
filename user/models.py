"""Module containing sqlalchemy models"""
from sqlalchemy import Column, String

from database.database import Base


class User(Base):
    """
    SqlAlchemy model
    """

    __tablename__ = "users"

    identifier = Column(String, primary_key=True, index=True)
    first_name = Column(String)
    last_name = Column(String)
