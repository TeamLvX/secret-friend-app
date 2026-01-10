from datetime import UTC, datetime

from pydantic import BaseModel, Field

from src.schema import AssignmentDetailsResponse, ParticipantDetailsResponse, Participant


class GameCreateRequest(BaseModel):
    name: str = Field(min_length=4, description="Game's name")
    description: str | None = Field(min_length=1, description="Game's optional description")
    host: str = Field(min_length=1, description="Game's organizer")
    exchange_date: datetime = Field(
        default_factory=lambda: UTC, description="Game's datetime to exchange gifs"
    )
    budget: float = Field(ge=0.0, description="Game's budget of the gifs")
    players: list[Participant] = Field(default_factory=list, description="Game's participants")

class GameDetailsResponse(BaseModel):
    """Class for keeping game details."""

    id: str
    name: str
    description: str
    host: str
    exchange_date: str
    budget: float
    participants: list[ParticipantDetailsResponse]
    assignments: list[AssignmentDetailsResponse]
