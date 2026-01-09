from pynamodb.attributes import UnicodeAttribute
from pynamodb.models import Model

from src.core.config import settings


class Participant(Model):
    class Meta:
        table_name = "participant_collection"
        host = settings.dynamodb_host
        region = settings.aws_region

    group_id = UnicodeAttribute(hash_key=True)
    id = UnicodeAttribute(range_key=True)
    name = UnicodeAttribute()
    alias = UnicodeAttribute(null=True)
    preferences = UnicodeAttribute(null=True)
