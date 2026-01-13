from fastapi import APIRouter, Depends, status

from src.core.dependencies import get_assignment_service, get_group_service
from src.schema import GameCreateRequest
from src.services import AssignmentService, GroupService

router = APIRouter()


@router.post("/")
def game_register(model: GameCreateRequest, service=Depends(get_group_service)):
    group_id = service.save(model)
    return group_id


@router.get("/{group_id}/join")
def group_join(group_id: str, service: GroupService = Depends(get_group_service)):
    return service.show_game_details(group_id)


@router.put("/{group_id}/assignments/{assignment_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_assignment(group_id: str, assignment_id: str, service: AssignmentService = Depends(get_assignment_service)):
    service.update_status(group_id, assignment_id)
