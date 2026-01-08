from dataclasses import dataclass
from typing import Optional

@dataclass
class ParticipantModel:
    id: str
    group_id: str
    name: str
    alias: Optional[str] = None
    preferences: Optional[str] = None

    @classmethod
    def create(cls, group_id:str, id:str, name:str, alias: Optional[str], preferences: Optional[str]):
        return cls(
            id = id,
            group_id = group_id,
            name = name,
            alias = alias,
            preferences = preferences
        )