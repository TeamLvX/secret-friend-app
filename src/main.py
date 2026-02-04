from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.api.exception_handlers import register_exception_handlers
from src.api.v1.router import api_router
from src.core.config import settings
from src.infrastructure.dynamodb.init_tables import init_tables


@asynccontextmanager
async def lifespan(app: FastAPI):
    """Lifespan event handler for startup and shutdown tasks."""
    print(f"[STARTUP] Environment: {settings.env}")
    print(f"[STARTUP] DynamoDB Endpoint: {settings.dynamodb_host or 'AWS Default'}")
    print(f"[STARTUP] AWS Region: {settings.aws_region}")
    print(f"[STARTUP] AWS Credentials: {'Configured' if settings.aws_access_key_id else 'Not Set'}")
    init_tables()
    yield


def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        lifespan=lifespan,
        version="0.1.0",
        description="Secret Friend App - Gift exchange application",
    )

    # Configure CORS middleware
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.cors_origins,
        allow_credentials=settings.cors_allow_credentials,
        allow_methods=settings.cors_allow_methods,
        allow_headers=settings.cors_allow_headers,
    )

    app.include_router(api_router, prefix="/api/v1")

    return app


app = create_app()
register_exception_handlers(app)
