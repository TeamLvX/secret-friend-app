from typing import Protocol
from src.models import AssignmentRead, AssignmentCreate, AssignmentsRead

class AssignmentRepository(Protocol):
    def save(self, assignment: AssignmentCreate) -> AssignmentRead:
        pass
    def get_by_group_id(self, group_id: str) -> AssignmentsRead | None:
        pass