from typing import Any

from boto3.dynamodb.types import TypeSerializer

serializer = TypeSerializer()


def serialize_item(item: dict[str, Any]) -> dict[str, Any]:
    return {k: serializer.serialize(v) for k, v in item.items()}
