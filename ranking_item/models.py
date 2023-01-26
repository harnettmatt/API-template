"""Module containing sqlalchemy models"""
from sqlalchemy import Column, ForeignKey, Table

from persistable.models import Base

rankings_items = Table(
    "rankings_items",
    Base.metadata,
    Column("ranking_id", ForeignKey("rankings.id"), primary_key=True),
    Column("item_id", ForeignKey("items.id"), primary_key=True),
)
