"""Routing handler for /users"""
from typing import List

from fastapi import APIRouter

from user.fixtures import get_mock_user
from user.model import User

ROUTER = APIRouter()


@ROUTER.get("/")
def get_all() -> List[User]:
    """
    gets all users
    @return: List[User]
    """
    return [get_mock_user()]
