from src.infrastructure.dynamodb.mappers import participant_to_domain
from src.infrastructure.dynamodb.models import ParticipantDynamoDBModel
from src.models import ParticipantModel

class ParticipantPynamoDBRepository:
    def save(self, participant: ParticipantModel) -> None:
        ParticipantDynamoDBModel(
            id = participant.id,
            group_id = participant.group_id,
            name = participant.name,
            alias = participant.alias,
            preferences = participant.preferences
        ).save()

    def get_by_id(self, group_id: str) -> ParticipantModel |  None:
        try:
            participant = ParticipantDynamoDBModel.get(group_id)
            return participant_to_domain(participant);
        except ParticipantDynamoDBModel.DoesNotExist:
            return None

    def get_list_by_id(self,group_id ) -> list[ParticipantModel]:
        participants = ParticipantDynamoDBModel.query(group_id)
        return [participant_to_domain(participant) for participant in participants];
        

    def get_by_group_id_and_participant_id(self,  group_id:str, participant_id:str) -> ParticipantModel | None:
        try:
            participant = ParticipantDynamoDBModel.get(group_id, participant_id);
            return participant_to_domain(participant);
        except ParticipantDynamoDBModel.DoesNotExist:
            return None