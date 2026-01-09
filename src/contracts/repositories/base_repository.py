from typing import Optional, Protocol, TypeVar

TModel = TypeVar('TModel', bound='Repository')

class Repository(Protocol[TModel]):
    def save(self, model: TModel) -> TModel:
        pass

    def get(self, arg1:str, arg2: Optional[str]) -> TModel | None:
        pass

    def get_list(self, arg:str) -> list[TModel] | None:
        pass