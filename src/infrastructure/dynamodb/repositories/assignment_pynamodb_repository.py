from uuid import uuid4

from pynamodb.exceptions import DoesNotExist

from src.contracts.repositories.base_repository import Repository
from src.core.exceptions import ResourceNotFound
from src.infrastructure.dynamodb.models import AssignmentPynamoDB
from src.models import Assignment


class AssignmentPynamoDBRepository(Repository[Assignment]):
    def save(self, assignment: Assignment) -> Assignment:
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
        return Assignment(
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

    def get(self, id: str, group_id: str) -> Assignment | None:
        try:
            item = AssignmentPynamoDB.get(group_id, id)
            return Assignment(
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
            raise ResourceNotFound

    def get_list(self, group_id: str) -> list[Assignment] | None:
        try:
            assignments: list[Assignment] = []
            for item in AssignmentPynamoDB.query(group_id):
                assignments.append(
                    Assignment(
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
            return assignments
        except DoesNotExist:
            return None
