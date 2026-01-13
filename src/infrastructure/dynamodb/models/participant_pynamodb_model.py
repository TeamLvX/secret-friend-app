from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model

from src.core.config import settings


class ParticipantPynamoDB(Model):
    class Meta:
        table_name = "participant_collection"
        host = settings.dynamodb_host
        region = settings.aws_region
        aws_access_key_id = settings.aws_access_key_id
        aws_secret_access_key = settings.aws_secret_access_key

    group_id = UnicodeAttribute(hash_key=True)
    id = UnicodeAttribute(range_key=True)
    name = UnicodeAttribute()
    alias = UnicodeAttribute(null=True)
    preferences = UnicodeAttribute(null=True)
