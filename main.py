"""Routing handler for /"""
from fastapi import FastAPI

from ranking.handler import ROUTER as RANKINGS_ROUTER
from rating.handler import ROUTER as RATINGS_ROUTER

APP = FastAPI()

APP.include_router(RANKINGS_ROUTER, prefix="/rankings")
APP.include_router(RATINGS_ROUTER, prefix="/ratings")
