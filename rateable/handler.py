"""Routing handler for /rateables"""
from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_session
from database.database_service import DatabaseService
from rateable import models, schemas

ROUTER = APIRouter()


@ROUTER.get("/", response_model=list[schemas.Rateable])
def get_all(session: Session = Depends(get_session)) -> Any:
    """
    Gets all rateables
    """
    return DatabaseService(session).all(model_type=models.Rateable)


@ROUTER.get("/{id}", response_model=schemas.Rateable)
def get(id: int, session: Session = Depends(get_session)) -> Any:
    """
    Gets a rateable by id
    """
    return DatabaseService(session).get(id=id, model_type=models.Rateable)


@ROUTER.post("/", response_model=schemas.Rateable)
def create(
    input: schemas.RateableCreate, session: Session = Depends(get_session)
) -> Any:
    """
    Creates a rateable
    """
    return DatabaseService(session).create(
        input_schema=input, model_type=models.Rateable
    )


@ROUTER.patch("/{id}", response_model=schemas.Rateable)
def update(
    id: int, input: schemas.RateableUpdate, session: Session = Depends(get_session)
) -> Any:
    """
    Patch a rateable by id
    """
    return DatabaseService(session).update(
        id=id, input_schema=input, model_type=models.Rateable
    )


@ROUTER.delete("/{id}", response_model=schemas.Rateable)
def delete(id: int, session: Session = Depends(get_session)) -> Any:
    """
    Deletes a rateable by id
    """
    return DatabaseService(session).delete(id=id, model_type=models.Rateable)
