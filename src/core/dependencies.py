from fastapi import Depends

from src.contracts.repositories import Repository
from src.services import AssignmentService, GameService
from src.infrastructure.dynamodb.repositories import AssignmentPynamoDBRepository, GroupPynamoDBRepository, ParticipantPynamoDBRepository


def get_assignment_repository() -> Repository:
    return AssignmentPynamoDBRepository()

def get_participant_repository() -> Repository:
    return ParticipantPynamoDBRepository

def get_group_repository() -> Repository:
    return GroupPynamoDBRepository()

def get_assignment_service(
        repo: Repository = Depends(get_assignment_repository)
) -> AssignmentService:
    return AssignmentService(repo)

def get_game_service(
        group_repository: Repository = Depends(get_assignment_repository),
        assignment_repository: Repository = Depends(get_assignment_repository),
        participant_repository: Repository = Depends(get_assignment_repository),
) -> GameService:
    return GameService(group_repository, assignment_repository, participant_repository)