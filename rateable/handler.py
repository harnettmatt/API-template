"""Routing handler for /rateables"""
from typing import List

from fastapi import APIRouter

from rateable.fixtures import get_mock_rateable
from rateable.model import Rateable

ROUTER = APIRouter()


@ROUTER.get("/")
def get_all() -> List[Rateable]:
    """
    gets all rateables
    @return: List[Rateable]
    """
    return [get_mock_rateable()]
