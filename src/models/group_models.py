from dataclasses import dataclass
from typing import List, Optional

@dataclass
class GroupModel:
    """Class for collecting entire group details and matching."""
    id: Optional[str]
    name: str
    description: str
    host: str
    exchange_date: str
    budget: float
    players: Optional[List]
    assignment: Optional[List]

@dataclass
class GroupCreate:
    """Class for creating new group document."""
    id: str
    name: str
    description: str
    exchange_date: str
    budget: float
    minimo: float

@dataclass
class GroupRead:
    """Class for collecting entire group details and assignments."""
    id: str
    name: str
    description: str
    host: str
    exchange_date: str
    budget: float
    players: Optional[List]
    assignment: Optional[List]
