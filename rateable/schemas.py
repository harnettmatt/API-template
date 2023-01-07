"""models for Rateable"""
from typing import List
from uuid import UUID

from uuid_base_model.schemas import UUIDBaseModel


class Rateable(UUIDBaseModel):
    """
    Pydantic model for Rateable
    """

    name: str
    ranking_ids: List[UUID] = []
