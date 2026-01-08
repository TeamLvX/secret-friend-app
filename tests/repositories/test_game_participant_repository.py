from src.infrastructure.dynamodb.models import GameParticipantModel
from src.infrastructure.dynamodb.repositories import GameParticipantPynamodb

def test_save_and_get_game_participant(mock_dynamodb_function):

    repo = GameParticipantPynamodb()

    game_participant = GameParticipantModel(
        game_id="123",
        participant_id="456",
        participant_name="John Doe",
        participant_alias="John Doe",
        participant_preferences="John Doe",
    )

    repo.save(game_participant)

    result = repo.get_by_id(game_participant.participant_id)

    assert result is not None
    assert result.participant_name == game_participant.participant_name
    assert result.participant_alias == game_participant.participant_alias
    assert result.participant_preferences == game_participant.participant_preferences