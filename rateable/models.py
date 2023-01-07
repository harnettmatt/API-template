"""Module containing sqlalchemy models"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from database.database import Base
from ranking_rateable.models import RankingRateable


class Rateable(Base):
    """
    SqlAlchemy model
    """

    __tablename__ = "rateables"

    identifier = Column(String, primary_key=True, index=True)
    name = Column(String)

    ratings = relationship("ratings", secondary=RankingRateable, backref="Rateable")
