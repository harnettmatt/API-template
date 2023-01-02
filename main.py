"""Routing handler for /"""
from fastapi import FastAPI

from rankings.handler import ROUTER as RANKINGS_ROUTER

APP = FastAPI()

APP.include_router(RANKINGS_ROUTER, prefix="/rankings")
