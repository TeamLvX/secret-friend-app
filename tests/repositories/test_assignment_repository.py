from datetime import datetime

import pytest

from src.infrastructure.dynamodb.repositories import (
    AssignmentPynamoDBRepository,
    GroupPynamoDBRepository,
)
from src.models import Assignment, Group


@pytest.fixture(scope="function", autouse=True)
def default_group_model(mock_dynamodb_function):
    repo = GroupPynamoDBRepository()

    return repo.save(
        Group.create(
            name="my secret santa group",
            description="we will play the secret santa gane in the office",
            exchange_date=datetime.now().isoformat(),
            host="psharpx",
            budget=100,
            players=None,
            assignments=None,
        )
    )


def test_save_and_get_assignment(default_group_model):
    repo = AssignmentPynamoDBRepository()

    assignment = repo.save(
        Assignment.create(
            group_id=default_group_model.id,
            giver_id="1",
            receiver_id="2",
            status=False,
        )
    )
    result = repo.get(assignment.id, default_group_model.id)

    assert result is not None
    assert result.id == assignment.id
    assert result.group_id == assignment.group_id
    assert result.giver_id == assignment.giver_id
    assert result.receiver_id == assignment.receiver_id
    assert result.status == assignment.status
    assert result.shown_at == assignment.shown_at


def test_save_and_get_assignment_by_group_id(default_group_model):
    repo = AssignmentPynamoDBRepository()

    stop = 6
    for item in range(1, stop):
        repo.save(
            Assignment.create(
                group_id=default_group_model.id,
                giver_id=str(item),
                receiver_id=str(stop - item),
                status=False,
            )
        )

    results = repo.get_list(default_group_model.id)
    assert results is not None
    assert len(results) == stop - 1
