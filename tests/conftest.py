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
from src.infrastructure.dynamodb.models import GroupDynamoDBModel, AssignmentDynamoDBModel, ParticipantDynamoDBModel

@pytest.fixture(scope="function", autouse=True)
def mock_dynamodb_function(monkeypatch):
    
    monkeypatch.setattr(GroupDynamoDBModel.Meta, "host", None)
    monkeypatch.setattr(AssignmentDynamoDBModel.Meta, "host", None)
    monkeypatch.setattr(ParticipantDynamoDBModel.Meta, "host", None)
    
    with mock_aws():
        try:
            if not GroupDynamoDBModel.exists():
                GroupDynamoDBModel.create_table(
                    read_capacity_units=1,
                    write_capacity_units=1,
                    wait=True)
        except Exception:
            pass

        try:
            if not AssignmentDynamoDBModel.exists():
                AssignmentDynamoDBModel.create_table(
                    read_capacity_units=1,
                    write_capacity_units=1,
                    wait=True)
        except Exception:
            pass
            
        try:
            if not ParticipantDynamoDBModel.exists():
                ParticipantDynamoDBModel.create_table(
                    read_capacity_units=1,
                    write_capacity_units=1,
                    wait=True)
        except Exception:
            pass

        yield