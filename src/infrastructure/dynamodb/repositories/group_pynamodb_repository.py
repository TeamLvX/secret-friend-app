from datetime import datetime
from uuid import uuid4

from pynamodb.exceptions import DoesNotExist

from src.contracts.repositories.base_repository import Repository
from src.core.exceptions import GroupNotFound
from src.infrastructure.dynamodb.models import GroupPynamoDB
from src.models import Group


class GroupPynamoDBRepository(Repository[Group]):
    def save(self, model: Group) -> Group:
        game_id = str(uuid4())
        # Convert string exchange_date to datetime for PynamoDB
        exchange_date_dt = datetime.fromisoformat(model.exchange_date) if isinstance(model.exchange_date, str) else model.exchange_date
        item = GroupPynamoDB(
            id=game_id,
            name=model.name,
            description=model.description,
            exchange_date=exchange_date_dt,
            host=model.host,
            budget=model.budget,
        )
        item.save()
        # Convert datetime back to ISO format string for domain model
        exchange_date_str = item.exchange_date.isoformat() if hasattr(item.exchange_date, "isoformat") else str(item.exchange_date)
        return Group(
            id=item.id,
            name=item.name,
            description=item.description,
            exchange_date=exchange_date_str,
            host=item.host,
            budget=item.budget,
            players=None,
            assignments=None,
        )

    def get(self, arg1: str, arg2: str | None) -> Group | None:
        try:
            item = GroupPynamoDB.get(arg1)
            # Convert datetime to ISO format string for domain model
            exchange_date_str = item.exchange_date.isoformat() if hasattr(item.exchange_date, "isoformat") else str(item.exchange_date)
            return Group(
                id=item.id,
                name=item.name,
                description=item.description,
                exchange_date=exchange_date_str,
                host=item.host,
                budget=item.budget,
                players=None,
                assignments=None,
            )
        except DoesNotExist:
            raise GroupNotFound(arg1)
