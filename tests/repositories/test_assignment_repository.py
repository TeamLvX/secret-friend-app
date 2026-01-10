import pytest
from datetime import datetime
from src.models import Group, Assignment
from src.infrastructure.dynamodb.repositories import GroupPynamoDBRepository, AssignmentPynamoDBRepository

@pytest.fixture(scope="function", autouse=True)
def default_group_model(mock_dynamodb_function):
    repo = GroupPynamoDBRepository()

    return repo.save(
        Group(
            id=None,
            name="my secret santa group",
            description="we will play the secret santa gane in the office",
            exchange_date=datetime.now(),
            host="psharpx",
            budget=100,
            players=None,
            assignment=None
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
            shown_at=None,
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
                receiver_id=str(stop-item),
                status=False,
                shown_at=None,
            )
        )

    results = repo.get_list(default_group_model.id)
    assert results is not None
    assert len(results) == stop - 1