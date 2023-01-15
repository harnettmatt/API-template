"""models for Ranking"""
from typing import List

from rateable.schemas import Rateable
from user.schemas import User
from uuid_base_model.schemas import UUIDBaseModel


class Ranking(UUIDBaseModel):
    """
    Pydantic model for Ranking
    """

    name: str
    author: User
    rateables: List[Rateable] = []
