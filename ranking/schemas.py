"""models for Ranking"""
from typing import List
from uuid import UUID

from user.schemas import User
from uuid_base_model.schemas import UUIDBaseModel


class Ranking(UUIDBaseModel):
    """
    Pydantic model for Ranking
    """

    name: str
    author: User
    rating_ids: List[UUID] = []
