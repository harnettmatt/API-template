"""Routing handler for /"""
from fastapi import FastAPI

from item.handler import ROUTER as ITEMS_ROUTER
from ranking.handler import ROUTER as RANKINGS_ROUTER
from user.handler import ROUTER as USERS_ROUTER

APP = FastAPI()

APP.include_router(RANKINGS_ROUTER, prefix="/rankings")
APP.include_router(ITEMS_ROUTER, prefix="/items")
APP.include_router(USERS_ROUTER, prefix="/users")
