"""Module containing sqlalchemy models"""
from sqlalchemy import Column, ForeignKey, String

from persistable.models import Persistable


class RankingRateable(Persistable):
    """
    SqlAlchemy model
    """

    __tablename__ = "rankings_rateables"

    identifier = Column(String, primary_key=True, index=True)
    rating_id = Column(String, ForeignKey("rankings.identifier"))
    author_id = Column(String, ForeignKey("rateables.identifier"))
