from pynamodb.attributes import NumberAttribute, UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model

from src.core.config import settings


class GroupPynamoDB(Model):
    class Meta:
        table_name = "group_collection"
        host = settings.dynamodb_host
        region = settings.aws_region

    id = UnicodeAttribute(hash_key=True, null=False)
    name = UnicodeAttribute(null=False)
    description = UnicodeAttribute(null=True)
    host = UnicodeAttribute(null=False)
    exchange_date = UTCDateTimeAttribute(null=False)
    budget = NumberAttribute(null=True, default=0)
