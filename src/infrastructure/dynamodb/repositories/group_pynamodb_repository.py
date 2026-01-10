from uuid import uuid4

from pynamodb.exceptions import DoesNotExist

from src.infrastructure.dynamodb.models import GroupPynamoDB
from src.models import GroupModel


class GroupPynamoDBRepository:
    def save(self, model: GroupModel) -> GroupModel:
        game_id = str(uuid4())
        item = GroupPynamoDB(
            id=game_id,
            name=model.name,
            description=model.description,
            exchange_date=model.exchange_date,
            host=model.host,
            budget=model.budget,
        )
        item.save()
        return GroupModel(
            id=item.id,
            name=item.name,
            description=item.description,
            exchange_date=item.exchange_date,
            host=item.host,
            budget=item.budget,
            players=None,
            assignment=None,
        )

    def get(self, identifier: str) -> GroupModel | None:
        try:
            item = GroupPynamoDB.get(identifier)
            return GroupModel(
                id=item.id,
                name=item.name,
                description=item.description,
                exchange_date=item.exchange_date,
                host=item.host,
                budget=item.budget,
                players=None,
                assignment=None,
            )
        except DoesNotExist:
            return None
