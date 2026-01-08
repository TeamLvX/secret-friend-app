from pynamodb.models import Model
from pynamodb.attributes import (UnicodeAttribute, BooleanAttribute, UTCDateTimeAttribute)
from src.core.config import settings

class AssignmentModel(Model):
    class Meta:
        table_name = "assignment_collection"
        host = settings.dynamodb_host
        region = settings.aws_region

    id = UnicodeAttribute(hash_key=True, null=False)
    group_id = UnicodeAttribute(null=False)
    giver_id = UnicodeAttribute(null=True)
    receiver_id = UnicodeAttribute(null=False)
    status = BooleanAttribute(default=False)
    shown_at = UTCDateTimeAttribute(null=True)