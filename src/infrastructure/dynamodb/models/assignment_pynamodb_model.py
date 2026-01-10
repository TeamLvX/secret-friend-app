from pynamodb.attributes import BooleanAttribute, UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model

from src.core.config import settings


class AssignmentPynamoDB(Model):
    class Meta:
        table_name = "assignment_collection"
        host = settings.dynamodb_host
        region = settings.aws_region

    id = UnicodeAttribute(hash_key=True)
    group_id = UnicodeAttribute()
    giver_id = UnicodeAttribute()
    receiver_id = UnicodeAttribute()
    status = BooleanAttribute(default=False)
    shown_at = UTCDateTimeAttribute(null=True)
