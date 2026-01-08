from typing import Protocol
from src.models import ParticipantModel


class ParticipantRepositoryContract(Protocol):
    def get_by_group_id_and_participant_id(self, group_id:str, participant_id:str) -> ParticipantModel | None:
        pass
