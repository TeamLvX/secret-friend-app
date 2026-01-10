from src.schema import ParticipantDetailsResponse
from src.models import Participant

def participant_to_schema(arg: Participant) -> ParticipantDetailsResponse:
    return ParticipantDetailsResponse(
        id=arg.id,
        name=arg.name,
        alias=arg.alias,
        preferences=arg.preferences,
    )