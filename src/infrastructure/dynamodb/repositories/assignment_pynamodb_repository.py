from uuid import uuid4
from typing import List
from pynamodb.exceptions import DoesNotExist

from src.infrastructure.dynamodb.models import AssignmentPynamoDB
from src.models import AssignmentModel, AssignmentsRead


class AssignmentPynamoDBRepository:
    def save(self, assignment: AssignmentModel) -> AssignmentModel:
        assignment_id = str(uuid4())
        item = AssignmentPynamoDB(
            id=assignment_id,
            group_id=assignment.group_id,
            giver_id=assignment.giver_id,
            receiver_id=assignment.receiver_id,
            status=assignment.status,
            shown_at=assignment.shown_at,
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

    def get(self, id: str, group_id: str) -> AssignmentModel | None:
        try:
            item = AssignmentPynamoDB.get(group_id, id)
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
        except DoesNotExist:
            return None

    def get_list(self, group_id: str) -> AssignmentsRead | None:
        try:
            assignments: List[AssignmentModel] = []
            for item in AssignmentPynamoDB.query(group_id):
                assignments.append(AssignmentModel(
                id=item.id,
                group_id=item.group_id,
                group_name=None,
                giver_id=item.giver_id,
                giver_name=None,
                receiver_id=item.receiver_id,
                receiver_name=None,
                status=item.status,
                shown_at=item.shown_at
            ))
            return AssignmentsRead(
                assignments=assignments
            )
        except DoesNotExist:
            return None
