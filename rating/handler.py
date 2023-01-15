"""Routing handler for /ratings"""
from typing import List

from fastapi import APIRouter

from rating.schemas import Rating
from rating.tests.fixtures import get_mock_rating

ROUTER = APIRouter()


@ROUTER.get("/")
def get_all() -> List[Rating]:
    """
    gets all ratings
    @return: List[Rating]
    """
    return [get_mock_rating()]
