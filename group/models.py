"""Module containing sqlalchemy models"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from item.models import Item  # noqa
from persistable.models import Persistable
from user.models import User  # noqa


class Group(Persistable):
    """
    SqlAlchemy model
    """

    __tablename__ = "groups"

    name = Column(String)
    items = relationship("Item", secondary="groups_items")
    # TODO: https://github.com/harnettmatt/rankings/issues/54
    # author_id = Column(Integer, ForeignKey("users.id"))
    # author = relationship("User")
