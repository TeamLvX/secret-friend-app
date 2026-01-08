import pytest
from datetime import datetime
from src.infrastructure.dynamodb.models import GroupModel, AssignmentModel
from src.infrastructure.dynamodb.repositories import GroupRepositoryPynamoDB, AssignmentRepositoryPynamoDB

@pytest.fixture(scope="function", autouse=True)
def default_group_model(mock_dynamodb_function):
    repo = GroupRepositoryPynamoDB()

    return repo.save(
        GroupModel(
            name="my secret santa group",
            description="we will play the secret santa gane in the office",
            exchange_date=datetime.now(),
            host="psharpx",
            budget=100,
        )
    )

def test_save_and_get_assignment(default_group_model):
    repo = AssignmentRepositoryPynamoDB()

    assignment = repo.save(
        AssignmentModel(
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
'''
def test_save_and_get_assignment_by_group_id(default_group_model):
    repo = AssignmentRepositoryPynamoDB()

    assignment1 = repo.save(
        AssignmentModel(
            group_id=default_group_model.id,
            giver_id="1",
            receiver_id="2",
            status=False,
            shown_at=None,
        )
    )
    assignment2 = repo.save(
        AssignmentModel(
            group_id=default_group_model.id,
            giver_id="2",
            receiver_id="1",
            status=False,
            shown_at=None,
        )
    )
    results = repo.get_by_group_id(default_group_model.id)

    assert results is not None
    assert len(results) == 2
    #assert result.group_id == assignment.group_id
    #assert result.giver_id == assignment.giver_id
    #assert result.receiver_id == assignment.receiver_id
    #assert result.status == assignment.status
    #assert result.shown_at == assignment.shown_at
'''