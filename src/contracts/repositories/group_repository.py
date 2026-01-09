from typing import Protocol

from src.models import GroupCreate, GroupRead


class GroupRepository(Protocol):
    def save(self, game: GroupCreate) -> GroupRead:
        pass

    def get_by_id(self, game_id: str) -> GroupRead | None:
        pass
