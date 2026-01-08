from dataclasses import dataclass
from typing import List, Optional

@dataclass
class AssignmentModel:
    """Class for keeping assignment details."""
    id: Optional[str]
    group_id: str
    group_name: Optional[str]
    giver_id: str
    giver_name: Optional[str]
    receiver_id: str
    receiver_name: Optional[str]
    status: Optional[bool]
    shown_at: Optional[str]

@dataclass
class AssignmentRead:
    """Class for keeping single assignment details."""
    id: str
    group_id: str
    group_name: Optional[str]
    giver_id: str
    giver_name: Optional[str]
    receiver_id: str
    receiver_name: Optional[str]
    status: Optional[bool]
    shown_at: Optional[str]

@dataclass
class AssignmentCreate:
    """Class for creating new group of assignment."""
    group_id: str
    giver_id: str
    receiver_id: str
    status: Optional[bool]
    shown_at: Optional[str]

@dataclass
class AssignmentsRead:
    """Class for collecting group of assignment details"""
    assignments: List[AssignmentModel]
