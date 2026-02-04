from pydantic import BaseModel, Field


class ParticipantCreateRequest(BaseModel):
    name: str = Field(description="Participant's name")
    alias: str | None = Field(default=None, description="Participant's optional alias")
    preferences: str | None = Field(description="Participant's option preferences")
    viewed: bool = Field(default=False, description="Assignment view status")


class ParticipantDetailsResponse(BaseModel):
    """Class for keeping Participant details."""

    id: str | None = Field(default=None, description="Participant's ID ")
    name: str = Field(description="Participant's name")
    alias: str | None = Field(default=None, description="Participant's alias")
    preferences: str | None = Field(default=None, description="Participant's preferences")
    viewed: bool = Field(description="Assignment view status")
