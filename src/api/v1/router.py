from fastapi import APIRouter

from src.api.v1.routes import health
from src.api.v1.routes import game

api_router = APIRouter()

api_router.include_router(health.router, prefix="/health", tags=["Health"])
api_router.include_router(game.router, prefix="/game", tags=["game"])
