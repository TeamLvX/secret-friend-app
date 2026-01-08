
from typing import Protocol, TypeVar

TModel = TypeVar('T', bound='GameRepository')

class GameRepository(Protocol[TModel]):
    def save(self, model: TModel) -> None:
        pass
    
    def get_by_id(self, id: str) -> TModel | None:
        pass