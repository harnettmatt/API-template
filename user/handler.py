"""Routing handler for /users"""
from typing import List

from fastapi import APIRouter

from database.database import get_session
from database.database_service import DatabaseService
from user.models import User as UserModel
from user.schemas import User as UserAPI

ROUTER = APIRouter()


@ROUTER.get("/")
def get_all() -> List[UserAPI]:
    """
    gets all users
    @return: List[User]
    """
    db_service = DatabaseService(get_session())
    users = db_service.all(model_type=UserModel)
    db_service.session.close()

    return [UserAPI(**user.__dict__) for user in users]


@ROUTER.post("/")
def create(user: UserAPI) -> UserAPI:
    """
    Creates a User
    """
    db_service = DatabaseService(get_session())
    model_instance = db_service.create(input_schema=user, model_type=UserModel)
    db_service.session.close()

    return UserAPI(**model_instance.__dict__)
