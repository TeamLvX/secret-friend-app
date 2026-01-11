from fastapi import APIRouter, Depends, HTTPException, status

from src.core.dependencies import get_assignment_service, get_group_service
from src.schema.game import GameCreateRequest

router = APIRouter()


@router.post("/")
def game_register(model: GameCreateRequest, service=Depends(get_group_service)):
    group_id = service.save(model)
    return group_id


@router.get("/{game_id}/join")
def game_join(game_id: str, service: Depends(get_group_service)):
    try:
        return service.show_game_details(game_id)
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )


@router.put("/{game_id}/assignments/{assignment_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_assignment(game_id: str, assignment_id: str, service=Depends(get_assignment_service)):
    try:
        service.update_status(game_id, assignment_id)
    except:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )
