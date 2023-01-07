"""models for Ranking"""
from typing import List

from rating.model import Rating
from user.model import User
from uuid_base_model.model import UUIDBaseModel


class Ranking(UUIDBaseModel):
    """
    Pydantic model for Ranking
    """

    name: str
    author: User
    ratings: List[Rating] = []
