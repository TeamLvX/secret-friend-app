from src.contracts.repositories import Repository
from src.infrastructure.dynamodb.mappers import participant_domain_to_paynamodb, participant_paynamodb_to_domain
from src.infrastructure.dynamodb.models import ParticipantPynamoDB
from src.infrastructure.dynamodb.transaction_context import DynamoDBTransactionContext
from src.models import Participant


class ParticipantPynamoDBRepository(Repository[Participant]):
    def save(self, participant: Participant) -> None:
        pynamodb_item = participant_domain_to_paynamodb(participant)

        transaction_context = DynamoDBTransactionContext.get_current()
        if transaction_context:
            transaction_context.save(pynamodb_item)
        else:
            pynamodb_item.save()

    def save_list(self, participants: list[Participant]) -> list[Participant]:
        transaction_context = DynamoDBTransactionContext.get_current()

        if transaction_context:
            for participant in participants:
                pynamodb_item = participant_domain_to_paynamodb(participant)
                transaction_context.save(pynamodb_item)
        else:
            with ParticipantPynamoDB.batch_write() as batch:
                for participant in participants:
                    pynamodb_item = participant_domain_to_paynamodb(participant)
                    batch.save(pynamodb_item)

        return participants

    def get(self, group_id: str, participant_id: str) -> Participant | None:
        try:
            participant = ParticipantPynamoDB.get(group_id, participant_id)
            return participant_paynamodb_to_domain(participant)
        except ParticipantPynamoDB.DoesNotExist:
            return None

    def get_list(self, group_id: str) -> list[Participant]:
        participants = ParticipantPynamoDB.query(group_id)
        return [participant_paynamodb_to_domain(participant) for participant in participants]
