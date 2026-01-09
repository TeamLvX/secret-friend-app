from dataclasses import dataclass


@dataclass
class AssignmentModel:
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

    assignments: list[AssignmentModel]
