"""models for Ranking"""
from typing import List

from pydantic import BaseModel


class Ranking(BaseModel):
    """
    Pydantic model for Ranking
    """

    name: str
    # TODO: type ratings
    ratings: List[dict] = []
