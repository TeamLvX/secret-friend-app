from datetime import datetime
from src.models import GroupModel
from src.infrastructure.dynamodb.repositories import GroupPynamoDBRepository

def test_save_and_get_group(mock_dynamodb_function):
    repo = GroupPynamoDBRepository()

    group = repo.save(
        GroupModel.create(
            name="my secret santa group",
            description="we will play the secret santa gane in the office",
            exchange_date=datetime.now(),
            host="psharpx",
            budget=100,
        )
    )
    result = repo.get(group.id)

    assert result is not None
    assert result.id == group.id
    assert result.name == group.name
    assert result.description == group.description
    assert result.budget == group.budget
    assert result.host == group.host
