"""models for Rating"""
from typing import Optional

from rateable.model import Rateable
from user.model import User
from uuid_base_model.model import UUIDBaseModel


class Rating(UUIDBaseModel):
    """
    Pydantic model for Rating
    """

    author: User
    recipient: Rateable
    rating: float
    notes: Optional[str] = None
