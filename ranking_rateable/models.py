"""Module containing sqlalchemy models"""
from sqlalchemy import Column, ForeignKey, String

from database.database import Base


class RankingRateable(Base):
    """
    SqlAlchemy model
    """

    __tablename__ = "rankings_rateables"

    identifier = Column(String, primary_key=True, index=True)
    rating_id = Column(String, ForeignKey("rankings.identifier"))
    author_id = Column(String, ForeignKey("rateables.identifier"))
