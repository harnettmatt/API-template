"""models for Rateable"""
from typing import List

from ranking.models import Ranking
from uuid_base_model.schemas import UUIDBaseModel


class Rateable(UUIDBaseModel):
    """
    Pydantic model for Rateable
    """

    name: str
    rankings: List[Ranking] = []
