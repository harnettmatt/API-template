"""Module containing sqlalchemy models"""
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from persistable.models import Persistable
from ranking_rateable.models import RankingRateable


class Ranking(Persistable):
    """
    SqlAlchemy model
    """

    __tablename__ = "rankings"

    name = Column(String)
    author_id = Column(String, ForeignKey("users.identifier"))

    ratings = relationship("ratings", secondary=RankingRateable, backref="Ranking")
