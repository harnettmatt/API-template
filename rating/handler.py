"""Routing handler for /ratings"""
from typing import List

from fastapi import APIRouter

from rating.fixtures import get_mock_rating
from rating.schemas import Rating

ROUTER = APIRouter()


@ROUTER.get("/")
def get_all() -> List[Rating]:
    """
    gets all ratings
    @return: List[Rating]
    """
    return [get_mock_rating()]
