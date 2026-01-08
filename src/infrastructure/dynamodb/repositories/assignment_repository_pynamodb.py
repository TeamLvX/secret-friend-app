from models import AssignmentModel
from src.repositories import AssignmentRepository
from src.infrastructure.dynamodb.models import AssignmentModel as AssignmentModelPynamoDB
from uuid import uuid4
from pynamodb.exceptions import DoesNotExist

class AssignmentRepositoryPynamoDB:
    def save(self, assignment: AssignmentModel) -> AssignmentModel:
        assignment_id = str(uuid4())
        item = AssignmentModelPynamoDB(
            id=assignment_id,
            group_id = assignment.group_id,
            giver_id = assignment.giver_id,
            receiver_id = assignment.receiver_id,
            status = assignment.status,
            shown_at = assignment.shown_at,
        )
        item.save()
        return AssignmentModel(
            id=item.id,
            group_id=item.group_id,
            group_name=None,
            giver_id=item.giver_id,
            giver_name=None,
            receiver_id=item.receiver_id,
            receiver_name=None,
            status=item.status,
            shown_at=item.shown_at,
        )

    def get_by_group_id(self, group_id: str) -> AssignmentModel | None:
        try:
            item = AssignmentModelPynamoDB.query(group_id)
            return None
            '''return GroupRead(
                id=item.id,
                name=item.name,
                description=item.description,
                exchange_date=item.exchange_date,
                host=item.host,
                budget=item.budget,
                players=None,
                assignment=None
            )'''
        except DoesNotExist:
            return None