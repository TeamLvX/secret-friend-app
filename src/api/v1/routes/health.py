from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()


class HealthResponse(BaseModel):
    """Health check response model."""

    status: str
    service: str = "Secret Friend App"


@router.get("/", response_model=HealthResponse, summary="Health Check", description="Check if the API is running and healthy", tags=["Health"])
def health() -> HealthResponse:
    """Health check endpoint.

    Returns:
        HealthResponse with status and service name
    """
    return HealthResponse(status="ok")
