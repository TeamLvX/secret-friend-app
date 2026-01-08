from typing import Protocol, TypeVar

TModel = TypeVar('TModel', bound='Repository')

class Repository(Protocol[TModel]):
    def save(self, model: TModel) -> TModel:
        pass

    def get_by_id(self, identifier: str) -> TModel | None:
        pass