from typing import Protocol
from src.models import GameModel

class GameRepository(Protocol):
    def save(self) -> None:
        pass
    def get_by_id(self, game_id: str) -> GameModel:
        pass