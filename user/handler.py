"""Routing handler for /users"""
from typing import List

from fastapi import APIRouter

from user.model import User

ROUTER = APIRouter()


def get_mock_user(identifier: str) -> User:
    """
    returns a mock user for temporary stubbing purposes
    @param identifier: specify an identifier to use for User object
    @return: User
    """
    return User(identifier=identifier, first_name="John", last_name="Smith")


@ROUTER.get("/")
def get_all() -> List[User]:
    """
    gets all users
    @return: List[User]
    """
    return [get_mock_user(identifier="fake-identifier")]


# @ROUTER.get("/{identifier}")
# def get(identifier: str) -> User:
#     """
#     gets user for identifier
#     @param identifier: id of the user to fetch
#     @return: User
#     """
#     return get_mock_user(identifier=identifier)
#
#
# @ROUTER.post("")
# def create_user(user: User) -> User:
#     """
#     creates a new User
#     @param: User
#     @return: User
#     """
#     return user
#
#
# # TODO: define patching model (ie: which attributes should be adjustable)
# @ROUTER.patch("/{identifier}")
# def patch_user(identifier: str) -> User:
#     """
#     patches specified user
#     @param identifier: id of the user to patch
#     @return: User
#     """
#     return get_mock_user(identifier=identifier)
#
#
# @ROUTER.delete("/{identifier}")
# def delete_user(identifier: str) -> User:
#     """
#     deletes specified user
#     @param identifier: id of the user to delete
#     @return: User
#     """
#     return get_mock_user(identifier)
