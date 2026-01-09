from src.infrastructure.dynamodb.mappers import participant_to_domain
from src.infrastructure.dynamodb.models import Participant as DynamoParticipant
from src.models import Participant


class ParticipantRepository:
    def save(self, participant: Participant) -> None:
        DynamoParticipant(
            group_id=participant.group_id,
            id=participant.id,
            name=participant.name,
            alias=participant.alias,
            preferences=participant.preferences,
        ).save()

    def get(self, group_id: str, participant_id: str) -> Participant | None:
        try:
            participant = DynamoParticipant.get(group_id, participant_id)
            return participant_to_domain(participant)
        except DynamoParticipant.DoesNotExist:
            return None

    def get_list(self, group_id: str) -> list[Participant]:
        participants = DynamoParticipant.query(group_id)
        return [participant_to_domain(participant) for participant in participants]
