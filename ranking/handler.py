"""Routing handler for /rankings"""
from typing import List

from fastapi import APIRouter

from ranking.fixtures import get_mock_ranking
from ranking.model import Ranking

ROUTER = APIRouter()


@ROUTER.get("/")
def get_all() -> List[Ranking]:
    """
    gets all rankings
    @return
    [
        {
            "name":
            "ratings": List[ratings]
        }
    ]
    """
    return [get_mock_ranking()]
