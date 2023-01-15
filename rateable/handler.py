"""Routing handler for /rateables"""
from typing import List

from fastapi import APIRouter

from rateable.schemas import Rateable
from rateable.tests.fixtures import get_mock_rateable

ROUTER = APIRouter()


@ROUTER.get("/")
def get_all() -> List[Rateable]:
    """
    gets all rateables
    @return: List[Rateable]
    """
    return [get_mock_rateable()]
