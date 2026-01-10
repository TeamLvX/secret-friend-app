from src.infrastructure.dynamodb.mappers import participant_to_domain
from src.infrastructure.dynamodb.models import ParticipantPynamoDB
from src.models import Participant


class ParticipantPynamoDBRepository:
    def save(self, participant: Participant) -> None:
        ParticipantPynamoDB(
            group_id=participant.group_id,
            id=participant.id,
            name=participant.name,
            alias=participant.alias,
            preferences=participant.preferences,
        ).save()

    def get(self, group_id: str, participant_id: str) -> Participant | None:
        try:
            participant = ParticipantPynamoDB.get(group_id, participant_id)
            return participant_to_domain(participant)
        except ParticipantPynamoDB.DoesNotExist:
            return None

    def get_list(self, group_id: str) -> list[Participant]:
        participants = ParticipantPynamoDB.query(group_id)
        return [participant_to_domain(participant) for participant in participants]
