from pynamodb.attributes import BooleanAttribute, UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model

from src.core.config import settings


class AssignmentPynamoDB(Model):
    class Meta:
        table_name = "assignment_collection"
        host = settings.dynamodb_host
        region = settings.aws_region
        aws_access_key_id = settings.aws_access_key_id or None
        aws_secret_access_key = settings.aws_secret_access_key or None

    group_id = UnicodeAttribute(hash_key=True)
    id = UnicodeAttribute(range_key=True)
    giver_id = UnicodeAttribute()
    receiver_id = UnicodeAttribute()
    status = BooleanAttribute(default=False)
    shown_at = UTCDateTimeAttribute(null=True)
    group_name = UnicodeAttribute(null=True)
    giver_name = UnicodeAttribute(null=True)
    receiver_name = UnicodeAttribute(null=True)
