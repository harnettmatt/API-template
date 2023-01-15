"""Module containing sqlalchemy models"""
from sqlalchemy import Column, ForeignKey, String
from sqlalchemy.dialects.postgresql import UUID
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
    author_id = Column(UUID, ForeignKey("users.identifier"))

    author = relationship("User")
    rateables = relationship("Rateable", secondary="rankings_rateables")
