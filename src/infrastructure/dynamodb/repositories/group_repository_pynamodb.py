from models import GroupModel
from src.infrastructure.dynamodb.models import GroupModel as GroupModelPynamoDB
from uuid import uuid4
from pynamodb.exceptions import DoesNotExist

class GroupRepositoryPynamoDB:
    def save(self, model: GroupModel) -> GroupModel:
        game_id = str(uuid4())
        item = GroupModelPynamoDB(
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
            assignment=None
        )

    def get_by_id(self, identifier: str) -> GroupModel | None:
        try:
            item = GroupModelPynamoDB.get(identifier)
            return GroupModel(
                id=item.id,
                name=item.name,
                description=item.description,
                exchange_date=item.exchange_date,
                host=item.host,
                budget=item.budget,
                players=None,
                assignment=None
            )
        except DoesNotExist:
            return None
