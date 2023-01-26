"""models for Ranking"""
from typing import List, Optional

from pydantic import BaseModel

from id_base_model.schemas import IDBaseModel
from item.schemas import Item


class Ranking(IDBaseModel):
    """
    Pydantic model for Ranking
    """

    name: str
    items: List[Item] = []
    # TODO: https://github.com/harnettmatt/rankings/issues/54
    # author: User

    class Config:
        orm_mode = True


class RankingCreate(BaseModel):
    name: str
    # TODO: https://github.com/harnettmatt/rankings/issues/54
    # author: User


class RankingUpdate(BaseModel):
    name: Optional[str] = None
