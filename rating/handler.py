"""Routing handler for /ratings"""
from typing import List

from fastapi import APIRouter

from rating.model import Rating

ROUTER = APIRouter()


def get_mock_rating(identifier: str) -> Rating:
    """
    returns a mock rating for temporary stubbing purposes
    @param identifier: specify an identifier to use for Rating object
    @return: Rating
    """
    return Rating(
        identifier=identifier,
        author="fake-author",
        recipient="fake-recipient",
        rating=1,
    )


@ROUTER.get("/")
def get_all() -> List[Rating]:
    """
    gets all ratings
    @return: List[Rating]
    """
    return [get_mock_rating(identifier="fake-identifier")]


#
# @ROUTER.get("/{identifier}")
# def get(identifier: str) -> Rating:
#     """
#     gets rating for identifier
#     @param identifier: id of the rating to fetch
#     @return: Rating
#     """
#     return get_mock_rating(identifier=identifier)
#
#
# @ROUTER.post("")
# def create_rating(rating: Rating) -> Rating:
#     """
#     creates a new rating
#     @param: Rating
#     @return: Rating
#     """
#     return rating
#
#
# # TODO: define patching model (ie: which attributes should be adjustable)
# @ROUTER.patch("/{identifier}")
# def patch_rating(identifier: str) -> Rating:
#     """
#     patches specified rating
#     @param identifier: id of the rating to patch
#     @return: Rating
#     """
#     return get_mock_rating(identifier=identifier)
#
#
# @ROUTER.delete("/{identifier}")
# def delete_rating(identifier: str) -> Rating:
#     """
#     deletes specified rating
#     @param identifier: id of the rating to delete
#     @return: Rating
#     """
#     return get_mock_rating(identifier)
