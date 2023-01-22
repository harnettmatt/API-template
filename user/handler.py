"""Routing handler for /users"""
from typing import Any

from fastapi import APIRouter

from database.database import get_session
from database.database_service import DatabaseService
from user import models, schemas

ROUTER = APIRouter()


@ROUTER.get("/", response_model=list[schemas.User])
def get_all() -> Any:
    """
    gets all users
    @return: List[User]
    """
    db_service = DatabaseService(get_session())
    users = db_service.all(model_type=models.User)
    db_service.session.close()

    return users


@ROUTER.get("/{id}", response_model=schemas.User)
def get(id: int) -> Any:
    """
    gets a user by id
    """
    db_service = DatabaseService(get_session())
    user = db_service.get(id=id, model_type=models.User)
    db_service.session.close()

    return user


@ROUTER.post("/", response_model=schemas.User)
def create(input: schemas.UserCreate) -> Any:
    """
    Creates a User
    """
    db_service = DatabaseService(get_session())
    user = db_service.create(input_schema=input, model_type=models.User)
    db_service.session.close()

    return user


@ROUTER.patch("/{id}", response_model=schemas.User)
def update(id: int, input: schemas.UserUpdate) -> Any:
    """
    Patches a User
    """
    db_service = DatabaseService(get_session())
    user = db_service.update(id=id, input_schema=input, model_type=models.User)
    db_service.session.close()

    return user


@ROUTER.delete("/{id}", response_model=schemas.User)
def delete(id: int) -> Any:
    """
    deletees a user by id
    """
    db_service = DatabaseService(get_session())
    user = db_service.delete(id=id, model_type=models.User)
    db_service.session.close()

    return user
