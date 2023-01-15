"""Module containing sqlalchemy models"""
from sqlalchemy import Column, ForeignKey, Table

from persistable.models import Base

rankings_ratings = Table(
    "rankings_ratings",
    Base.metadata,
    Column("ranking_id", ForeignKey("rankings.identifier"), primary_key=True),
    Column("rating_id", ForeignKey("ratings.identifier"), primary_key=True),
)
