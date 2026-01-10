from pydantic import BaseModel, Field
from typing import Optional

class Assignment(BaseModel):
    id: str | None = Field(description="")
    group_id: str = Field(description="")
    group_name: str | None = Field(description="")
    giver_id: str = Field(description="")
    giver_name: str | None = Field(description="")
    receiver_id: str = Field(description="")
    receiver_name: str | None = Field(description="")
    status: bool | None = Field(description="")
    shown_at: str | None = Field(description="")

class AssignmentDetailsResponse(BaseModel):
    """Class for keeping assignments details."""

    id: str | None = Field(description="ID of the assignment")
    giver_id: str = Field(description="ID of the giver participant")
    giver_name: str | None = Field(description="Name of giver participant")
    receiver_id: str = Field(description="ID of the receiver participant")
    receiver_name: str | None = Field(description="ID of the receiver participant")
    status: bool | None = Field(description="Shown status of the assignment")
    shown_at: Optional[str] | None = Field(description="")
