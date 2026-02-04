from fastapi import APIRouter, Depends, Query, status

from src.core.dependencies import get_assignment_service, get_group_service
from src.schema import AssignmentDetailsResponse, GameCreateRequest, GameDetailsResponse
from src.services import AssignmentService, GroupService

router = APIRouter()


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    response_model=dict,
    summary="Create a new game",
    description="Register a new Secret Friend game with participants and exchange details",
)
def game_register(model: GameCreateRequest, service: GroupService = Depends(get_group_service)) -> dict:
    group_id = service.save_game(model)
    return {"group_id": group_id}


@router.get(
    "/{group_id}/join",
    response_model=GameDetailsResponse,
    summary="Get game details",
    description="Retrieve complete details of a Secret Friend game including participants and assignments",
)
def group_join(group_id: str, service: GroupService = Depends(get_group_service)) -> GameDetailsResponse:
    return service.show_game_details(group_id)


@router.get(
    "/{group_id}/assignment/{player_id}",
    response_model=AssignmentDetailsResponse,
    summary="Get assigment deatails by player",
    description="Retrieve complete details of the assignment by player",
)
def assigment_details(group_id: str, player_id: str, service: AssignmentService = Depends(get_assignment_service)) -> AssignmentDetailsResponse:
    return service.get_assigmnet_player(group_id, player_id)


@router.put(
    "/{group_id}/assignment/{assignment_id}",
    status_code=status.HTTP_204_NO_CONTENT,
    summary="Update assignment status",
    description="Mark an assignment as completed or update its status",
)
def update_assignment(
    group_id: str,
    assignment_id: str,
    player_id: str = Query(..., description="The player ID"),
    service: AssignmentService = Depends(get_assignment_service),
) -> None:
    service.update_status(group_id, assignment_id, player_id)
