from dataclasses import dataclass


@dataclass
class Participant:
    id: str
    group_id: str
    name: str
    alias: str | None = None
    preferences: str | None = None

    @classmethod
    def create(cls, group_id: str, id: str, name: str, alias: str | None, preferences: str | None):
        return cls(id=id, group_id=group_id, name=name, alias=alias, preferences=preferences)
