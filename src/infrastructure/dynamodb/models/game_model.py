from pynamodb.models import Model
from pynamodb.attributes import (UnicodeAttribute, BooleanAttribute, NumberAttribute, UTCDateTimeAttribute)

class GameModel(Model):
    class Meta:
        table_name = "game_collection"

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