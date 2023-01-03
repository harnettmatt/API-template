"""Routing handler for /rateables"""
from typing import List

from fastapi import APIRouter

from rateable.model import Rateable

ROUTER = APIRouter()


def get_mock_rateable(identifier: str) -> Rateable:
    """
    returns a mock rateable for temporary stubbing purposes
    @param identifier: specify an identifier to use for Rateable object
    @return: Rateable
    """
    return Rateable(
        identifier=identifier,
        name="fake-rateable",
    )


@ROUTER.get("/")
def get_all() -> List[Rateable]:
    """
    gets all rateables
    @return: List[Rateable]
    """
    return [get_mock_rateable(identifier="fake-identifier")]


# @ROUTER.get("/{identifier}")
# def get(identifier: str) -> Rateable:
#     """
#     gets rateable for identifier
#     @param identifier: id of the rateable to fetch
#     @return: Rateable
#     """
#     return get_mock_rateable(identifier=identifier)
#
#
# @ROUTER.post("")
# def create_rateable(rateable: Rateable) -> Rateable:
#     """
#     creates a new Rateable
#     @param: Rateable
#     @return: Rateable
#     """
#     return rateable
#
#
# # TODO: define patching model (ie: which attributes should be adjustable)
# @ROUTER.patch("/{identifier}")
# def patch_rateable(identifier: str) -> Rateable:
#     """
#     patches specified rateable
#     @param identifier: id of the rateable to patch
#     @return: Rateable
#     """
#     return get_mock_rateable(identifier=identifier)
#
#
# @ROUTER.delete("/{identifier}")
# def delete_rateable(identifier: str) -> Rateable:
#     """
#     deletes specified rateable
#     @param identifier: id of the rateable to delete
#     @return: Rateable
#     """
#     return get_mock_rateable(identifier)
