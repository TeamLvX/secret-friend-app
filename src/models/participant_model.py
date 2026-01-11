from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Participant:
    group_id: str
    name: str
    alias: str | None = None
    preferences: str | None = None
    id: str | None = None

    @classmethod
    def create(
        cls,
        group_id: str,
        name: str,
        alias: str | None,
        preferences: str | None,
        id: str | None = None,
    ):
        if id is None:
            id = str(uuid4())
        return cls(group_id=group_id, name=name, alias=alias, preferences=preferences, id=id)
