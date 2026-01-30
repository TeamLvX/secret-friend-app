from src.infrastructure.dynamodb.models import AssignmentPynamoDB
from src.models import Assignment


def assignment_domain_to_pyanmodb(model: Assignment) -> AssignmentPynamoDB:
    return AssignmentPynamoDB(
        group_id=model.group_id,
        id=model.id,
        giver_id=model.giver_id,
        receiver_id=model.receiver_id,
        status=model.status,
        shown_at=model.shown_at,
        group_name=model.group_name,
        giver_name=model.giver_name,
        receiver_name=model.receiver_name,
    )


def assignment_paynamodb_to_domain(paynamodb_model: AssignmentPynamoDB) -> Assignment:
    return Assignment.create(
        id=paynamodb_model.id,
        group_id=paynamodb_model.group_id,
        group_name=paynamodb_model.group_name,
        giver_id=paynamodb_model.giver_id,
        giver_name=paynamodb_model.giver_name,
        receiver_id=paynamodb_model.receiver_id,
        receiver_name=paynamodb_model.receiver_name,
        status=paynamodb_model.status,
        shown_at=paynamodb_model.shown_at,
    )
