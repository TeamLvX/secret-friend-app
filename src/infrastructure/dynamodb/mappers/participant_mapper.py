from src.infrastructure.dynamodb.models import Participant as DynamoParticipant
from src.models import Participant


def participant_to_domain(dynamoModel: DynamoParticipant) -> Participant:
    return Participant.create(
        group_id=dynamoModel.group_id,
        id=dynamoModel.id,
        name=dynamoModel.name,
        alias=dynamoModel.alias,
        preferences=dynamoModel.preferences,
    )
