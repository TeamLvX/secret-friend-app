import datetime

from src.contracts.repositories import Repository
from src.models import Assignment


class AssignmentService:
    def __init__(self, assignment_repository: Repository):
        self.assignment_repository = assignment_repository

    def update_status(self, group_id: str, assignment_id: str):
        item: Assignment = self.assignment_repository.get(assignment_id, group_id)

        exchange_date_str = datetime.datetime.now()

        item.status = True
        item.shown_at = exchange_date_str
        self.assignment_repository.save(item)
