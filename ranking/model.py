"""models for Ranking"""
from typing import List

from pydantic import BaseModel

from rating.model import Rating


class Ranking(BaseModel):
    """
    Pydantic model for Ranking
    """

    name: str
    ratings: List[Rating] = []
