"""Module containing sqlalchemy models"""
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.orm import relationship

from database.database import Base
from ranking_rateable.models import RankingRateable


class Ranking(Base):
    """
    SqlAlchemy model
    """

    __tablename__ = "rankings"

    identifier = Column(String, primary_key=True, index=True)
    name = Column(String)
    author_id = Column(String, ForeignKey("users.identifier"))

    ratings = relationship("ratings", secondary=RankingRateable, backref="Ranking")
