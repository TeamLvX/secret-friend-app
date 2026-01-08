from typing import Protocol, TypeVar

TModel = TypeVar('TModel', bound='AssignmentRepository')

class AssignmentRepository(Protocol[TModel]):
    def get_by_group_id(self, group_id: str) -> TModel | None:
        pass