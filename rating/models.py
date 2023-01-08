"""Module containing sqlalchemy models"""
from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.orm import relationship

from persistable.models import Persistable
from rateable.schemas import Rateable
from user.schemas import User


class Rating(Persistable):
    """
    SqlAlchemy model
    """

    __tablename__ = "ratings"

    author_id = Column(String, ForeignKey("users.identifier"))
    recipient_id = Column(String, ForeignKey("rateables.identifier"))
    rating = Column(Float)
    notes = Column(String)

    author = relationship("users", secondary=User, backref="Rating")
    recipient = relationship("rateables", secondary=Rateable, backref="Rating")
