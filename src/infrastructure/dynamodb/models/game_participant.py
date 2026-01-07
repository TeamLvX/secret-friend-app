from pynamodb.models import Model
from pynamodb.attributes import UnicodeAttribute
from src.core.config import settings

class GameParticipantModel(Model):
    class Meta:
        table_name = "game_participant"
        host = settings.dynamodb_host
        region = settings.aws_region

    game_id: UnicodeAttribute(hash_key=True)
    participant_id: UnicodeAttribute(range_key=True)
    participant_name: UnicodeAttribute()
    participant_alias: UnicodeAttribute(null=True)
    participant_preferences: UnicodeAttribute(null=True)