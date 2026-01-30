from pynamodb.exceptions import DoesNotExist

from src.contracts.repositories.base_repository import Repository
from src.core.exceptions import ResourceNotFound
from src.infrastructure.dynamodb.mappers import assignment_domain_to_pyanmodb, assignment_paynamodb_to_domain
from src.infrastructure.dynamodb.models import AssignmentPynamoDB
from src.infrastructure.dynamodb.transaction_context import DynamoDBTransactionContext
from src.models import Assignment


class AssignmentPynamoDBRepository(Repository[Assignment]):
    def save(self, assignment: Assignment) -> Assignment:
        item = assignment_domain_to_pyanmodb(assignment)

        transaction_context = DynamoDBTransactionContext.get_current()
        if transaction_context:
            transaction_context.save(item)
        else:
            item.save()

        return assignment_paynamodb_to_domain(item)

    def get(self, id: str, group_id: str) -> Assignment | None:
        try:
            item = AssignmentPynamoDB.get(group_id, id)
            return assignment_paynamodb_to_domain(item)
        except DoesNotExist:
            raise ResourceNotFound

    def save_list(self, assignments: list[Assignment]) -> list[Assignment]:
        transaction_context = DynamoDBTransactionContext.get_current()

        if transaction_context:
            for assignment in assignments:
                item = assignment_domain_to_pyanmodb(assignment)
                transaction_context.save(item)
        else:
            with AssignmentPynamoDB.batch_write() as batch:
                for assignment in assignments:
                    item = assignment_domain_to_pyanmodb(assignment)
                    batch.save(item)

        return assignments

    def get_list(self, group_id: str) -> list[Assignment] | None:
        try:
            assignments = [assignment_paynamodb_to_domain(item) for item in AssignmentPynamoDB.query(group_id)]
            return assignments
        except DoesNotExist:
            return None
