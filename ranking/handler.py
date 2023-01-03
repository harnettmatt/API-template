"""Routing handler for /rankings"""
from typing import List

from fastapi import APIRouter

from ranking.model import Ranking

ROUTER = APIRouter()


@ROUTER.get("/")
def get_all() -> List[Ranking]:
    """
    gets all rankings
    @return
    [
        {
            "name":
            "ratings": List[ratings]
        }
    ]
    """
    return [Ranking(name="fake-name")]


#
# @ROUTER.get("/{name}")
# def get(name: str) -> Ranking:
#     """
#     gets ranking
#     @param name: ranking to be returned
#     @return
#     [
#         {
#             "name":
#             "ratings": List[ratings]
#         }
#     ]
#     """
#     return Ranking(name=name)
#
#
# @ROUTER.post("")
# def create_ranking(ranking: Ranking) -> Ranking:
#     """
#     creates a new ranking
#     @param: Ranking
#     @return: Ranking
#     """
#     return ranking
#
#
# @ROUTER.patch("/{name}")
# def patch_ranking(name: str) -> Ranking:
#     """
#     patches specified ranking
#     @param name: name (uuid) of ranking
#     @return:
#     {
#         "name": str
#         "ratings": List[ratings]
#     }
#     """
#     return Ranking(name=name)
#
#
# @ROUTER.delete("/{name}")
# def delete_ranking(name: str) -> Ranking:
#     """
#     deletes specified ranking
#     @param name: name (uuid) of ranking
#     @return:
#     {
#         "name": str
#         "ratings": List[ratings]
#     }
#     """
#     return Ranking(name=name)
