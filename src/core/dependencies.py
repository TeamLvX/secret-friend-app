from fastapi import Depends

from src.contracts.repositories import Repository
from src.infrastructure.dynamodb.repositories import (
    AssignmentPynamoDBRepository,
    GroupPynamoDBRepository,
    ParticipantPynamoDBRepository,
)
from src.models import Assignment, Group, Participant
from src.services import AssignmentService, GroupService


def get_assignment_repository() -> Repository[Assignment]:
    return AssignmentPynamoDBRepository()


def get_participant_repository() -> Repository[Participant]:
    return ParticipantPynamoDBRepository


def get_group_repository() -> Repository[Group]:
    return GroupPynamoDBRepository()


def get_assignment_service(repo: Repository[Assignment] = Depends(get_assignment_repository)) -> AssignmentService:
    return AssignmentService(repo)


def get_group_service(
    group_repository: Repository[Group] = Depends(get_assignment_repository),
    assignment_repository: Repository[Assignment] = Depends(get_assignment_repository),
    participant_repository: Repository[Participant] = Depends(get_assignment_repository),
) -> GroupService:
    return GroupService(group_repository, assignment_repository, participant_repository)
