"""Routing handler for /rankings"""
from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_session
from database.database_service import DatabaseService
from ranking import models, schemas

ROUTER = APIRouter()


@ROUTER.get("/", response_model=list[schemas.Ranking])
def get_all(session: Session = Depends(get_session)) -> Any:
    """
    Gets all rankings
    """
    return DatabaseService(session).all(model_type=models.Ranking)


@ROUTER.get("/{id}", response_model=schemas.Ranking)
def get(id: int, session: Session = Depends(get_session)) -> Any:
    """
    Gets a ranking by id
    """
    return DatabaseService(session).get(id=id, model_type=models.Ranking)


@ROUTER.post("/", response_model=schemas.Ranking)
def create(
    input: schemas.RankingCreate, session: Session = Depends(get_session)
) -> Any:
    """
    Creates a ranking
    """
    return DatabaseService(session).create(
        input_schema=input, model_type=models.Ranking
    )


@ROUTER.patch("/{id}", response_model=schemas.Ranking)
def update(
    id: int, input: schemas.RankingUpdate, session: Session = Depends(get_session)
) -> Any:
    """
    Patch a ranking by id
    """
    return DatabaseService(session).update(
        id=id, input_schema=input, model_type=models.Ranking
    )


@ROUTER.delete("/{id}", response_model=schemas.Ranking)
def delete(id: int, session: Session = Depends(get_session)) -> Any:
    """
    Deletes a ranking by id
    """
    return DatabaseService(session).delete(id=id, model_type=models.Ranking)
