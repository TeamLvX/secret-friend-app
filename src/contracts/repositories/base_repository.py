from typing import Protocol, TypeVar

TModel = TypeVar('TModel', bound='Repository')

class Repository(Protocol[TModel]):
    def save(self, model: TModel) -> TModel:
        pass

    def get_by_id(self, identifier: str) -> TModel | None:
        pass

    def get_list_by_id(self, identifier:str) -> list[TModel] | None:
        pass