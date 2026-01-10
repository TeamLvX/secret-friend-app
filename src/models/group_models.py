from dataclasses import dataclass
from typing import Optional, List


@dataclass
class Group:
    """Class for collecting entire group details and matching."""

    id: str | None
    name: str
    description: str
    host: str
    exchange_date: str
    budget: float
    players: list | None
    assignment: list | None


    @classmethod
    def create(cls, name: str, description: str, host: str, exchange_date: str, budget: float, id: Optional[str] = None, players: Optional[List] = None, assignment: Optional[List] = None):
        return cls(
            id=id,
            name=name,
            description=description,
            host=host,
            exchange_date=exchange_date,
            budget=budget,
            players=players,
            assignment=assignment
        )

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
