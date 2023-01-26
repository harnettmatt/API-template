"""Module containing sqlalchemy models"""
from sqlalchemy import Column, ForeignKey, Integer

from persistable.models import Persistable


class Membership(Persistable):
    __tablename__ = "memberships"

    group_id = Column(Integer, ForeignKey("groups.id"))
    item_id = Column(Integer, ForeignKey("items.id"))
