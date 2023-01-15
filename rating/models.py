"""Module containing sqlalchemy models"""
from sqlalchemy import Column, Float, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from persistable.models import Persistable
from rateable.models import Rateable  # noqa
from user.models import User  # noqa


class Rating(Persistable):
    """
    SqlAlchemy model
    """

    __tablename__ = "ratings"

    author_id = Column(UUID, ForeignKey("users.identifier"))
    recipient_id = Column(UUID, ForeignKey("rateables.identifier"))
    rating = Column(Float)
    notes = Column(String)

    author = relationship("User")
    recipient = relationship("Rateable")
