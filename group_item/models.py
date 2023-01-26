"""Module containing sqlalchemy models"""
from sqlalchemy import Column, ForeignKey, Table

from persistable.models import Base

groups_items = Table(
    "groups_items",
    Base.metadata,
    Column("group_id", ForeignKey("groups.id"), primary_key=True),
    Column("item_id", ForeignKey("items.id"), primary_key=True),
)
