from src.contracts.repositories import Repository
from src.models import Group
from src.schema import GameDetailsResponse, AssignmentDetailsResponse, ParticipantDetailsResponse
from src.mappers import assignment_to_schema, participant_to_schema


class GameService:
    def __init__(self, group_repository: Repository, assignment_repository: Repository, participant_repository: Repository):
        self.assignment_repository = assignment_repository
        self.group_repository = group_repository
        self.participant_repository = participant_repository

    def show_game_details(self, group_id: str) -> GameDetailsResponse | None:
        try:
            item: Group = self.group_repository.get(group_id, None)
            assignments: list[AssignmentDetailsResponse] = [assignment_to_schema(x) for x in self.assignment_repository.get_list(group_id)]
            participants: list[ParticipantDetailsResponse] = [participant_to_schema(x) for x in self.participant_repository.get_list(group_id)]

            return GameDetailsResponse(
                id=item.id,
                name=item.name,
                description=item.description,
                host=item.host,
                exchange_date=item.exchange_date,
                budget=item.budget,
                participants=participants,
                assignments=assignments
            )
        except Exception as e:
            pass