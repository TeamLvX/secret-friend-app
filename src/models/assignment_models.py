from typing import Optional
from dataclasses import dataclass


@dataclass
class Assignment:
    """Class for keeping assignment details."""

    id: str | None
    group_id: str
    group_name: str | None
    giver_id: str
    giver_name: str | None
    receiver_id: str
    receiver_name: str | None
    status: bool | None
    shown_at: str | None


    @classmethod
    def create(cls, group_id: str, giver_id: str, receiver_id: str, status: Optional[bool], shown_at: Optional[str], id: Optional[str] = None, group_name: Optional[str] = None, giver_name: Optional[str] = None, receiver_name: Optional[str] = None):
        return cls(
            id=id,
            group_id=group_id,
            group_name=group_name,
            giver_id=giver_id,
            giver_name=giver_name,
            receiver_id=receiver_id,
            receiver_name=receiver_name,
            status=status,
            shown_at=shown_at
        )

@dataclass
class AssignmentRead:
    """Class for keeping single assignment details."""

    id: str
    group_id: str
    group_name: str | None
    giver_id: str
    giver_name: str | None
    receiver_id: str
    receiver_name: str | None
    status: bool | None
    shown_at: str | None


@dataclass
class AssignmentCreate:
    """Class for creating new group of assignment."""

    group_id: str
    giver_id: str
    receiver_id: str
    status: bool | None
    shown_at: str | None


@dataclass
class AssignmentsRead:
    """Class for collecting group of assignment details"""

    assignments: list[Assignment]
