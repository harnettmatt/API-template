"""Module containing sqlalchemy models"""
from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from database.database import Base
from rateable.schemas import Rateable
from user.schemas import User


class Rating(Base):
    """
    SqlAlchemy model
    """

    __tablename__ = "ratings"

    identifier = Column(String, primary_key=True, index=True)
    author_id = Column(String, ForeignKey("users.identifier"))
    recipient_id = Column(String, ForeignKey("rateables.identifier"))
    rating = Column(Float)
    notes = Column(String)

    author = relationship("users", secondary=User, backref="Rating")
    recipient = relationship("rateables", secondary=Rateable, backref="Rating")
