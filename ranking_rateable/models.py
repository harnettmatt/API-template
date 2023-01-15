"""Module containing sqlalchemy models"""
from sqlalchemy import Column, ForeignKey, Table

from persistable.models import Base

rankings_rateables = Table(
    "rankings_rateables",
    Base.metadata,
    Column("ranking_id", ForeignKey("rankings.identifier"), primary_key=True),
    Column("rateable_id", ForeignKey("rateables.identifier"), primary_key=True),
)
