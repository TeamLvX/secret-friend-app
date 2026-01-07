from fastapi import FastAPI
from src.core.config import settings
from src.api.v1.router import api_router

def create_app() -> FastAPI:
    app = FastAPI(
        tittle=settings.app_name,
        debug=settings.debug
    )
    
    app.include_router(api_router, prefix="/api/v1")
    return app

app = create_app()