from src.infrastructure.dynamodb.models import ParticipantPynamoDB
from src.models import Participant


def participant_to_domain(dynamoModel: ParticipantPynamoDB) -> Participant:
    return Participant.create(
        group_id=dynamoModel.group_id,
        id=dynamoModel.id,
        name=dynamoModel.name,
        alias=dynamoModel.alias,
        preferences=dynamoModel.preferences,
    )
