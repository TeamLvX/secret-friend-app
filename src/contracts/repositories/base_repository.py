from typing import Generic, Protocol, TypeVar

TModel = TypeVar("TModel")


class Repository(Protocol, Generic[TModel]):
    def save(self, model: TModel) -> TModel:
        pass

    def save_list(self, list_model: list[TModel]) -> list[TModel]:
        pass

    def get(self, arg1: str, arg2: str | None) -> TModel | None:
        pass

    def get_list(self, arg: str) -> list[TModel] | None:
        pass
