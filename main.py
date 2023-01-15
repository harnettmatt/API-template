"""Routing handler for /"""
from fastapi import FastAPI

from ranking.handler import ROUTER as RANKINGS_ROUTER
from rateable.handler import ROUTER as RATEABLES_ROUTER
from user.handler import ROUTER as USERS_ROUTER

APP = FastAPI()

APP.include_router(RANKINGS_ROUTER, prefix="/rankings")
APP.include_router(RATEABLES_ROUTER, prefix="/rateables")
APP.include_router(USERS_ROUTER, prefix="/users")
