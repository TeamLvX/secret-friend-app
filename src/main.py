from contextlib import asynccontextmanager

from fastapi import FastAPI

from src.api.exception_handlers import register_exception_handlers
from src.api.v1.router import api_router
from src.core.config import settings
from src.infrastructure.dynamodb.init_tables import init_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler for startup and shutdown tasks."""
    init_tables()
    yield


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name, lifespan=lifespan)

    app.include_router(api_router, prefix="/api/v1")

    return app


app = create_app()
register_exception_handlers(app)
