"""Module containing sqlalchemy models"""
from sqlalchemy import Column, String

from database.database import Base


class Rateable(Base):
    """
    SqlAlchemy model
    """

    __tablename__ = "rateables"

    identifier = Column(String, primary_key=True, index=True)
    name = Column(String)
