from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Assignment:
    """Class for keeping assignment details."""

    group_id: str
    giver_id: str
    receiver_id: str
    group_name: str | None
    giver_name: str | None
    receiver_name: str | None
    status: bool | None
    shown_at: str | None
    id: str | None

    @classmethod
    def create(
        cls,
        group_id: str,
        giver_id: str,
        receiver_id: str,
        group_name: str | None = None,
        giver_name: str | None = None,
        receiver_name: str | None = None,
        status: bool = False,
        shown_at: str | None = None,
        id: str | None = None,
    ):
        if id is None:
            id = str(uuid4())
        return cls(
            group_id=group_id,
            giver_id=giver_id,
            receiver_id=receiver_id,
            group_name=group_name,
            giver_name=giver_name,
            receiver_name=receiver_name,
            status=status,
            shown_at=shown_at,
            id=id,
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
