from fastapi import APIRouter, Depends, Path, Query, HTTPException, status

from src.core import get_game_service, get_assignment_service
from src.services import GameService, AssignmentService

router = APIRouter()

@router.get("/{game_id}/join")
def game_join(game_id: str, service: GameService = Depends(get_game_service)):
    try:
        return service.show_game_details(game_id)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,)

@router.put("/{game_id}/assignments/{assignment_id}", status_code=status.HTTP_204_NO_CONTENT)
def update_assignment(game_id: str, assignment_id: str, service: AssignmentService = Depends(get_assignment_service)):
    try:
        service.update_status(game_id, assignment_id)
    except:
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,)
