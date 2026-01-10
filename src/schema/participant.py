from pydantic import BaseModel, Field
from typing import Optional


class Participant(BaseModel):
    group_id: str = Field(description="Game's groupdId")
    id: str | None = Field(description="Participant's ID ")
    name: str = Field(description="Participant's name")
    alias: str | None = Field(description="Participant's optional alias")
    preferences: str | None = Field(description="Participant's option preferences")

class ParticipantDetailsResponse(BaseModel):
    """Class for keeping Participant details."""

    id: str | None = Field(description="Participant's ID ")
    name: str = Field(description="Participant's name")
    alias: Optional[str] | None = Field(description="Participant's alias")
    preferences: Optional[str] | None = Field(description="Participant's preferences")
