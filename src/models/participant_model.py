from dataclasses import dataclass
from uuid import uuid4


@dataclass
class Participant:
    group_id: str
    name: str
    alias: str | None = None
    preferences: str | None = None
    id: str | None = None
    viewed: bool = False

    @classmethod
    def create(
        cls,
        group_id: str,
        name: str,
        alias: str | None,
        preferences: str | None,
        viewed: bool | None = None,
        id: str | None = None,
    ):
        if id is None:
            id = str(uuid4())
        if viewed is None:
            viewed = False
        return cls(group_id=group_id, name=name, alias=alias, preferences=preferences, id=id, viewed=viewed)
