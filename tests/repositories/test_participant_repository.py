

from src.infrastructure.dynamodb.repositories import ParticipantPynamoDBRepository
from src.models import ParticipantModel

def test_save_and_get_game_participant(mock_dynamodb_function):

    repo = ParticipantPynamoDBRepository()

    participant = ParticipantModel(
        group_id="123",
        id="456",
        name="John Doe",
        alias="John Doe",
        preferences="John Doe",
    )

    repo.save(participant)

    result = repo.get_by_group_id_and_participant_id(participant.group_id, participant.id)

    assert result is not None
    assert result.name == participant.name
    assert result.alias == participant.alias
    assert result.preferences == participant.preferences