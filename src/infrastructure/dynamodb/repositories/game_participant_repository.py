from src.infrastructure.dynamodb.models.game_participant import GameParticipantModel

class GameParticipantPynamodb:
    def save(self, game_participant: GameParticipantModel) -> None:
        game_participant.save()
        
    def get_by_id(self, participant_id: str) -> GameParticipantModel | None:
        try:
            return GameParticipantModel.get(participant_id)
        except GameParticipantModel.DoesNotExist:
            return None

        