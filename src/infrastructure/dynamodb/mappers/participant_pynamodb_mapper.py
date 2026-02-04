from src.infrastructure.dynamodb.models import ParticipantPynamoDB
from src.models import Participant


def participant_paynamodb_to_domain(dynamoModel: ParticipantPynamoDB) -> Participant:
    return Participant.create(
        group_id=dynamoModel.group_id,
        id=dynamoModel.id,
        name=dynamoModel.name,
        alias=dynamoModel.alias,
        preferences=dynamoModel.preferences,
        viewed=dynamoModel.viewed,
    )


def participant_domain_to_paynamodb(model: Participant) -> ParticipantPynamoDB:
    return ParticipantPynamoDB(
        group_id=model.group_id, id=model.id, name=model.name, alias=model.alias, preferences=model.preferences, viewed=model.viewed
    )
