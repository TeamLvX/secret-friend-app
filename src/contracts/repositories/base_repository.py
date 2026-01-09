from typing import Protocol, TypeVar

TModel = TypeVar("TModel", bound="Repository")


class Repository(Protocol[TModel]):
    def save(self, model: TModel) -> TModel:
        pass

    def get(self, arg1: str, arg2: str | None) -> TModel | None:
        pass

    def get_list(self, arg: str) -> list[TModel] | None:
        pass
