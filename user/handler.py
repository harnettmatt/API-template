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
    Getse all users
    """
    return DatabaseService().all(model_type=models.User)


@ROUTER.get("/{id}", response_model=schemas.User)
def get(id: int) -> Any:
    """
    Gets a user by id
    """
    return DatabaseService(get_session()).get(id=id, model_type=models.User)


@ROUTER.post("/", response_model=schemas.User)
def create(input: schemas.UserCreate) -> Any:
    """
    Creates a user
    """
    return DatabaseService(get_session()).create(
        input_schema=input, model_type=models.User
    )


@ROUTER.patch("/{id}", response_model=schemas.User)
def update(id: int, input: schemas.UserUpdate) -> Any:
    """
    Patch a user by id
    """
    return DatabaseService(get_session()).update(
        id=id, input_schema=input, model_type=models.User
    )


@ROUTER.delete("/{id}", response_model=schemas.User)
def delete(id: int) -> Any:
    """
    Deletes a user by id
    """
    return DatabaseService(get_session()).delete(id=id, model_type=models.User)
