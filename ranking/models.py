"""Module containing sqlalchemy models"""
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from persistable.models import Persistable
from rating.models import Rating  # noqa


class Ranking(Persistable):
    """
    SqlAlchemy model
    """

    __tablename__ = "rankings"

    name = Column(String)
    author_id = Column(UUID, ForeignKey("users.identifier"))

    ratings = relationship("Rating", secondary="rankings_ratings")
