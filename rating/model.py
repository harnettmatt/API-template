"""models for Rating"""
from typing import Optional

from pydantic import BaseModel


class Rating(BaseModel):
    """
    Pydantic model for Rating
    """

    identifier: str  # TODO: uuid
    author: str  # TODO: type author as a "user"
    recipient: str  # TODO: type recipient as a "rateable object"
    rating: float
    notes: Optional[str]
