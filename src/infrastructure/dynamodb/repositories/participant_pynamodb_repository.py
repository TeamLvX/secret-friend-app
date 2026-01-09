from src.infrastructure.dynamodb.mappers import participant_to_domain
from src.infrastructure.dynamodb.models import ParticipantDynamoDBModel
from src.models import ParticipantModel

class ParticipantPynamoDBRepository:
    def save(self, participant: ParticipantModel) -> None:
        ParticipantDynamoDBModel(
            group_id = participant.group_id,
            id = participant.id,
            name = participant.name,
            alias = participant.alias,
            preferences = participant.preferences
        ).save()

    def get(self, group_id: str, participant_id:str) -> ParticipantModel |  None:
        try:
            participant = ParticipantDynamoDBModel.get(group_id, participant_id)
            return participant_to_domain(participant)
        except ParticipantDynamoDBModel.DoesNotExist:
            return None

    def get_list(self, group_id:str) -> list[ParticipantModel]:
        participants = ParticipantDynamoDBModel.query(group_id)
        return [participant_to_domain(participant) for participant in participants]