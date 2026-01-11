from dataclasses import dataclass
from uuid import uuid4

from .assignment_models import Assignment
from .participant_model import Participant


@dataclass
class Group:
    """Class for collecting entire group details and matching."""

    name: str
    host: str
    exchange_date: str
    budget: float
    players: list[Participant] | None = None
    assignments: list[Assignment] | None = None
    id: str | None = None
    description: str | None = None

    @classmethod
    def create(
        cls,
        name: str,
        host: str,
        exchange_date: str,
        budget: float,
        players: list[Participant] | None,
        assignments: list[Assignment] | None,
        id: str | None = None,
        description: str | None = None,
    ):
        if id is None:
            id = str(uuid4())
        return cls(
            name=name,
            host=host,
            exchange_date=exchange_date,
            budget=budget,
            players=players,
            assignments=assignments,
            id=id,
            description=description,
        )
