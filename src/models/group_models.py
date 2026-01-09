from dataclasses import dataclass


@dataclass
class GroupModel:
    """Class for collecting entire group details and matching."""

    id: str | None
    name: str
    description: str
    host: str
    exchange_date: str
    budget: float
    players: list | None
    assignment: list | None


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
    players: list | None
    assignment: list | None
