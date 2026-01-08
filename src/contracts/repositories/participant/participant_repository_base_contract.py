from typing import Protocol
from src.contracts.repositories.base_repository import Repository
from src.contracts.repositories.participant.participant_repository_contract import ParticipantRepositoryContract

class ParticipantRepositoryBaseContract(Repository, ParticipantRepositoryContract, Protocol):
    pass