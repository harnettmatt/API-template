"""models for Ranking"""
from typing import List

from rating.schemas import Rating
from user.schemas import User
from uuid_base_model.schemas import UUIDBaseModel


class Ranking(UUIDBaseModel):
    """
    Pydantic model for Ranking
    """

    name: str
    author: User
    ratings: List[Rating] = []
