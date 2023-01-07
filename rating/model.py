"""models for Rating"""
from typing import Optional

from uuid_base_model.model import UUIDBaseModel


class Rating(UUIDBaseModel):
    """
    Pydantic model for Rating
    """

    author: str  # TODO: type author as a "user"
    recipient: str  # TODO: type recipient as a "rateable object"
    rating: float
    notes: Optional[str] = None
