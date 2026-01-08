from pynamodb.models import Model
from pynamodb.attributes import (UnicodeAttribute, BooleanAttribute, NumberAttribute, UTCDateTimeAttribute)
from src.core.config import settings

class GameModel(Model):
    class Meta:
        table_name = "game_collection"
        host = settings.dynamodb_host
        region = settings.aws_region

'''
    name:
    ":"
    string
    ",
    "description": "string",
    "host": "string",
    "date": "string",
    "minimo": 0,

'''