
from src.infrastructure.dynamodb.models import ParticipantDynamoDBModel
from src.models import ParticipantModel

def participant_to_domain(dynamoModel: ParticipantDynamoDBModel) -> ParticipantModel:
    return ParticipantModel.create(
        group_id = dynamoModel.group_id,
        id = dynamoModel.id,
        name = dynamoModel.name,
        alias = dynamoModel.alias,
        preferences=dynamoModel.preferences
    )
