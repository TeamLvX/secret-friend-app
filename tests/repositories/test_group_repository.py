from datetime import datetime

from src.infrastructure.dynamodb.repositories import GroupPynamoDBRepository
from src.models import Group


def test_save_and_get_group(mock_dynamodb_function):
    repo = GroupPynamoDBRepository()

    group = repo.save(
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
    result = repo.get(group.id, arg2=None)

    assert result is not None
    assert result.id == group.id
    assert result.name == group.name
    assert result.description == group.description
    assert result.budget == group.budget
    assert result.host == group.host
