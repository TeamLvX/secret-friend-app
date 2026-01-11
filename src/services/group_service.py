from src.contracts.repositories.base_repository import Repository
from src.mappers import assignment_to_schema, participant_to_schema
from src.models import Assignment, Group, Participant
from src.schema import AssignmentDetailsResponse, GameCreateRequest, GameDetailsResponse, ParticipantDetailsResponse
from src.shared import random_cycle_assigments


class GroupService:
    def __init__(
        self,
        group_repo: Repository[Group],
        assignment_repo: Repository[Assignment],
        participant_repo: Repository[Participant],
    ):
        self.group_repository = group_repo
        self.assignment_repository = assignment_repo
        self.participant_repository = participant_repo

    def save_game(self, group_data: GameCreateRequest) -> str:
        group = Group.create(
            name=group_data.name,
            host=group_data.name,
            exchange_date=group_data.exchange_date,
            budget=group_data.budget,
        )

        # saving group
        group_result = self.group_repository.save(group)

        # saving participants
        players = [
            Participant.create(
                group_id=group_result.group_id,
                name=player.name,
                alias=player.alias,
                preferences=player.preferences,
            )
            for player in group_data.players
        ]

        participants_result = self.participant_repository.save_list(players)

        # saving assignments
        player_names = [player.name for player in participants_result]
        players_by_name = {p.name: p for p in players}
        assignments_random = random_cycle_assigments(player_names)

        assigments = [
            Assignment.create(
                group_id=group_data.id,
                giver_id=players_by_name[a[0]].id,
                receiver_id=players_by_name[a[1]].id,
                group_name=group_data.name,
                giver_name=players_by_name[a[0]].name,
                receiver_name=players_by_name[a[1]].name,
            )
            for a in assignments_random
        ]

        self.assignment_repository.save_list(assigments)

        return group_result.id

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
                assignments=assignments,
            )
        except Exception:
            pass
