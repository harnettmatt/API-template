"""Routing handler for /"""
from fastapi import FastAPI

from ranking.handler import ROUTER as RANKINGS_ROUTER

APP = FastAPI()

APP.include_router(RANKINGS_ROUTER, prefix="/ranking")
