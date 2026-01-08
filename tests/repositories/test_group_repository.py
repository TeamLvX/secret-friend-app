from datetime import datetime
from src.infrastructure.dynamodb.models import GroupModel
from src.infrastructure.dynamodb.repositories import GroupRepositoryPynamoDB

def test_save_and_get_group(mock_dynamodb_function):
    repo = GroupRepositoryPynamoDB()

    group = repo.save(
        GroupModel(
            name="my secret santa group",
            description="we will play the secret santa gane in the office",
            exchange_date=datetime.now(),
            host="psharpx",
            budget=100,
        )
    )
    result = repo.get_by_id(group.id)

    assert result is not None
    assert result.id == group.id
    assert result.name == group.name
    assert result.description == group.description
    assert result.budget == group.budget
    assert result.host == group.host