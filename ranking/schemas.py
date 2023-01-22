"""models for Ranking"""
from typing import List

from id_base_model.schemas import IDBaseModel
from rateable.schemas import Rateable
from user.schemas import User


class Ranking(IDBaseModel):
    """
    Pydantic model for Ranking
    """

    name: str
    author: User
    rateables: List[Rateable] = []
