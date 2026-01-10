from uuid import uuid4

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

    def get_by_id(self, id: str) -> AssignmentModel | None:
        try:
            print(id)
            item = AssignmentPynamoDB.get(id, range_key=None)
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

    def get_by_group_id(self, group_id: str) -> AssignmentsRead | None:
        try:
            assignments: list[AssignmentModel] = []
            for item in AssignmentPynamoDB.query(None, AssignmentPynamoDB.group_id == group_id):
                assignments.append(
                    AssignmentModel(
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
                )

            return AssignmentsRead(assignments=assignments)
        except DoesNotExist:
            return None
