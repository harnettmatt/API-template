"""models for Rating"""
from typing import Optional
from uuid import UUID

from uuid_base_model.schemas import UUIDBaseModel


class Rating(UUIDBaseModel):
    """
    Pydantic model for Rating
    """

    author_id: UUID
    recipient_id: UUID
    rating: float
    notes: Optional[str] = None
