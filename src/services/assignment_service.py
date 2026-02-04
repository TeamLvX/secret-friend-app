import datetime

from src.contracts.repositories import Repository
from src.infrastructure.dynamodb.transaction_context import DynamoDBTransactionContext
from src.mappers import assignment_to_schema
from src.models import Assignment, Participant


class AssignmentService:
    def __init__(
        self,
        assignment_repo: Repository[Assignment],
        participant_repo: Repository[Participant],
    ):
        self.assignment_repository = assignment_repo
        self.participant_repo = participant_repo

    def update_status(self, group_id: str, assignment_id: str, player_id: str):
        with DynamoDBTransactionContext.begin():
            assignmentData: Assignment = self.assignment_repository.get(assignment_id, group_id)

            exchange_date_str = datetime.datetime.now()
            assignmentData.status = True
            assignmentData.shown_at = exchange_date_str
            self.assignment_repository.save(assignmentData)

            participanData: Participant = self.participant_repo.get(group_id, player_id)
            participanData.viewed = True
            self.participant_repo.save(participanData)

    def get_assigmnet_player(self, group_id: str, player_id: str):
        items: list[Assignment] = self.assignment_repository.get_list(group_id)

        player_assignment = next((item for item in items if item.giver_id == player_id), None)

        return assignment_to_schema(player_assignment)
