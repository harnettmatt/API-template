"""models for Rating"""
from typing import Optional

from rateable.schemas import Rateable
from user.schemas import User
from uuid_base_model.schemas import UUIDBaseModel


class Rating(UUIDBaseModel):
    """
    Pydantic model for Rating
    """

    author: User
    recipient: Rateable
    rating: float
    notes: Optional[str] = None
