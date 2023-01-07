"""Module containing sqlalchemy models"""
from sqlalchemy import Column, Float, ForeignKey, String

from database.database import Base


class Rating(Base):
    """
    SqlAlchemy model
    """

    __tablename__ = "ratings"

    identifier = Column(String, primary_key=True, index=True)
    author_id = Column(String, ForeignKey("users.identifer"))
    recipient_id = Column(String, ForeignKey("rateables.identifier"))
    rating = Column(Float)
    notes = Column(String)
