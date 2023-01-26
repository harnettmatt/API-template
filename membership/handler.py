"""Routing handler for /memberships"""
from typing import Any

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from database.database import get_session
from database.database_service import DatabaseService
from membership import models, schemas

ROUTER = APIRouter()


@ROUTER.get("/", response_model=list[schemas.Membership])
def get_all(session: Session = Depends(get_session)) -> Any:
    """
    Gets all memberships
    """
    return DatabaseService(session).all(model_type=models.Membership)


@ROUTER.get("/{id}", response_model=schemas.Membership)
def get(id: int, session: Session = Depends(get_session)) -> Any:
    """
    Gets a membership by id
    """
    return DatabaseService(session).get(id=id, model_type=models.Membership)


@ROUTER.post("/", response_model=schemas.Membership)
def create(
    input: schemas.MembershipCreate, session: Session = Depends(get_session)
) -> Any:
    """
    Creates a membership
    """
    return DatabaseService(session).create(
        input_schema=input, model_type=models.Membership
    )


@ROUTER.patch("/{id}", response_model=schemas.Membership)
def update(
    id: int, input: schemas.MembershipUpdate, session: Session = Depends(get_session)
) -> Any:
    """
    Patch a membership by id
    """
    return DatabaseService(session).update(
        id=id, input_schema=input, model_type=models.Membership
    )


@ROUTER.delete("/{id}", response_model=schemas.Membership)
def delete(id: int, session: Session = Depends(get_session)) -> Any:
    """
    Deletes a membership by id
    """
    return DatabaseService(session).delete(id=id, model_type=models.Membership)
