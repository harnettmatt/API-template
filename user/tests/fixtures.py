"""Module containing helpful object constructors for mocking purposes"""
from database.database import get_session
from database.database_service import DatabaseService
from user import models, schemas
from utilities.tests.fixtures import get_mock_id


def get_mock_user(id: int = get_mock_id()) -> schemas.User:
    """
    returns a mock User
    @param id: specify an id to use for User object
    @return: User
    """
    return schemas.User(id=id, first_name="John", last_name="Smith")


def create_user() -> models.User:
    user_input = schemas.UserCreate(first_name="John", last_name="Smith")
    return DatabaseService(get_session()).create(
        input_schema=user_input, model_type=models.User
    )
