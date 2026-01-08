import os
import pytest

# Set environment variables before any imports that use settings
os.environ.setdefault("AWS_REGION", "us-east-1")
os.environ.setdefault("AWS_DEFAULT_REGION", "us-east-1")
os.environ.setdefault("DYNAMODB_HOST", "")  # Empty for moto to intercept
os.environ.setdefault("APP_NAME", "Secret Friend App")
os.environ.setdefault("ENV", "test")
os.environ.setdefault("DEBUG", "true")
os.environ.setdefault("AWS_ACCESS_KEY_ID", "testing")
os.environ.setdefault("AWS_SECRET_ACCESS_KEY", "testing")
os.environ.setdefault("AWS_SECURITY_TOKEN", "testing")
os.environ.setdefault("AWS_SESSION_TOKEN", "testing")

from moto import mock_aws
from src.infrastructure.dynamodb.models.game_model import GameModel
from src.infrastructure.dynamodb.models.game_participant import GameParticipantModel

@pytest.fixture(scope="function", autouse=True)
def mock_dynamodb_function(monkeypatch):
    
    monkeypatch.setattr(GameModel.Meta, "host", None)
    monkeypatch.setattr(GameParticipantModel.Meta, "host", None)
    
    with mock_aws():
        try:
            if not GameModel.exists():
                GameModel.create_table(
                    read_capacity_units=1,
                    write_capacity_units=1,
                    wait=True)
        except Exception:
            pass
            
        try:
            if not GameParticipantModel.exists():
                GameParticipantModel.create_table(
                    read_capacity_units=1,
                    write_capacity_units=1,
                    wait=True)
        except Exception:
            pass
            
        yield