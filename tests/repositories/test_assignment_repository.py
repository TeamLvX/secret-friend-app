from datetime import datetime

import pytest

from src.infrastructure.dynamodb.models import AssignmentPynamoDB, GroupPynamoDB
from src.infrastructure.dynamodb.repositories import (
    AssignmentPynamoDBRepository,
    GroupPynamoDBRepository,
)


@pytest.fixture(scope="function", autouse=True)
def default_group_model(mock_dynamodb_function):
    repo = GroupPynamoDBRepository()

    return repo.save(
        GroupPynamoDB(
            name="my secret santa group",
            description="we will play the secret santa gane in the office",
            exchange_date=datetime.now(),
            host="psharpx",
            budget=100,
        )
    )


def test_save_and_get_assignment(default_group_model):
    repo = AssignmentPynamoDBRepository()

    assignment = repo.save(
        AssignmentPynamoDB(
            group_id=default_group_model.id,
            giver_id="1",
            receiver_id="2",
            status=False,
            shown_at=None,
        )
    )
    result = repo.get_by_id(assignment.id)

    assert result is not None
    assert result.id == assignment.id
    assert result.group_id == assignment.group_id
    assert result.giver_id == assignment.giver_id
    assert result.receiver_id == assignment.receiver_id
    assert result.status == assignment.status
    assert result.shown_at == assignment.shown_at
