from src.models import Assignment
from src.schema import AssignmentDetailsResponse


def assignment_to_schema(arg: Assignment) -> AssignmentDetailsResponse:
    return AssignmentDetailsResponse(
        id=arg.id,
        giver_id=arg.giver_id,
        giver_name=arg.giver_name,
        receiver_id=arg.receiver_id,
        receiver_name=arg.giver_name,
        status=arg.status,
        shown_at=arg.shown_at,
    )
