"""Routing handler for /rankings"""
from typing import List

from fastapi import APIRouter

from ranking.schemas import Ranking
from ranking.tests.fixtures import get_mock_ranking

ROUTER = APIRouter()


@ROUTER.get("/")
def get_all() -> List[Ranking]:
    """
    gets all rankings
    @return
    [
        {
            "name":
            "rateables": List[Rateable]
        }
    ]
    """
    return [get_mock_ranking()]
