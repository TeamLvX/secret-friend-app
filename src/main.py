from fastapi import FastAPI

from src.api.exception_handlers import register_exception_handlers
from src.api.v1.router import api_router
from src.core.config import settings


def create_app() -> FastAPI:
    app = FastAPI(title=settings.app_name)

    app.include_router(api_router, prefix="/api/v1")
    return app


app = create_app()
register_exception_handlers(app)
