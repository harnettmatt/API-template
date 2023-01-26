"""Module containing sqlalchemy models"""
from sqlalchemy import Column, ForeignKey, Table

from persistable.models import Base

memberships = Table(
    "memberships",
    Base.metadata,
    Column("group_id", ForeignKey("groups.id"), primary_key=True),
    Column("item_id", ForeignKey("items.id"), primary_key=True),
)
