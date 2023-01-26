"""Module containing sqlalchemy models"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from item.models import Item  # noqa
from persistable.models import Persistable
from user.models import User  # noqa


class Ranking(Persistable):
    """
    SqlAlchemy model
    """

    __tablename__ = "rankings"

    name = Column(String)
    items = relationship("Item", secondary="rankings_items")
    # TODO: https://github.com/harnettmatt/rankings/issues/54
    # author_id = Column(Integer, ForeignKey("users.id"))
    # author = relationship("User")
