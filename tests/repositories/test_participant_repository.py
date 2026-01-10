from src.infrastructure.dynamodb.repositories import ParticipantPynamoDBRepository
from src.models import Participant


def test_save_and_get_by_id():
    repo = ParticipantPynamoDBRepository()

    participant = Participant(
        group_id="123",
        id="456",
        name="John Doe",
        alias="John Doe",
        preferences="John Doe",
    )

    repo.save(participant)

    result = repo.get(participant.group_id, participant.id)

    assert result is not None
    assert result.name == participant.name
    assert result.alias == participant.alias
    assert result.preferences == participant.preferences


def test_save_and_get_list_by_group_id():
    repo = ParticipantPynamoDBRepository()

    participant = Participant(
        group_id="123",
        id="456",
        name="John Doe",
        alias="John Doe",
        preferences="John Doe",
    )

    repo.save(participant)

    result = repo.get_list("123")

    assert result is not None
    assert result[0].name == participant.name
    assert result[0].alias == participant.alias
    assert result[0].preferences == participant.preferences
