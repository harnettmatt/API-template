"""Module contains an abstract base class for objects that can be persisted"""
from sqlalchemy import Column, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Persistable(Base):  # type: ignore
    """
    Abstract class that defines the minimum attributes to be persistable
    """

    # TODO: does this need to be typed as absract so it can't be instantiated?

    __tablename__ = "abstract"

    identifier = Column(String, primary_key=True, index=True)
