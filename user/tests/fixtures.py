"""Module containing helpful object constructors for mocking purposes"""
from uuid import UUID

from database.database import get_session
from database.database_service import DatabaseService
from user.models import User as UserModel
from user.schemas import User as UserSchema
from utilities.tests.fixtures import get_mock_uuid


def get_mock_user(identifier: UUID = get_mock_uuid()) -> UserSchema:
    """
    returns a mock User
    @param identifier: specify an identifier to use for User object
    @return: User
    """
    return UserSchema(identifier=identifier, first_name="John", last_name="Smith")


def create_user() -> UserModel:
    user_input = UserSchema(first_name="John", last_name="Smith")
    return DatabaseService(get_session()).create(
        input_schema=user_input, model_type=UserModel
    )
