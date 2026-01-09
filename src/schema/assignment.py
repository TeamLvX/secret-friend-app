from pydantic import BaseModel, Field


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
