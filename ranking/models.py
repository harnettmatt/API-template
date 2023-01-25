"""Module containing sqlalchemy models"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from persistable.models import Persistable
from rateable.models import Rateable  # noqa
from user.models import User  # noqa


class Ranking(Persistable):
    """
    SqlAlchemy model
    """

    __tablename__ = "rankings"

    name = Column(String)
    rateables = relationship("Rateable", secondary="rankings_rateables")
    # TODO: https://github.com/harnettmatt/rankings/issues/54
    # author_id = Column(Integer, ForeignKey("users.id"))
    # author = relationship("User")
