import boto3
import pytest
from botocore.exceptions import ClientError, EndpointConnectionError

from src.core.config import settings


def test_dynamodb_connection():
    endpoint_url = "http://localhost:4566"

    dynamodb_client = boto3.client(
        "dynamodb",
        endpoint_url=endpoint_url,
        region_name=settings.aws_region,
        aws_access_key_id="dummy",
        aws_secret_access_key="dummy",
    )

    try:
        response = dynamodb_client.list_tables()
        assert "TableNames" in response
        assert isinstance(response["TableNames"], list)
    except EndpointConnectionError:
        pytest.skip("LocalStack is not running. Skipping connection test.")
    except ClientError as e:
        error_code = e.response.get("Error", {}).get("Code", "")
        if error_code not in ["ResourceNotFoundException", "AccessDeniedException"]:
            pytest.fail(f"DynamoDB client error: {e}")


def test_dynamodb_connection_with_settings():
    endpoint_url = "http://localhost:8001"

    # Verify settings are loaded correctly
    assert settings.aws_region is not None
    assert settings.aws_region == "us-east-1"

    # Create client with settings
    dynamodb_client = boto3.client(
        "dynamodb",
        endpoint_url=endpoint_url,
        region_name=settings.aws_region,
        aws_access_key_id="dummy",
        aws_secret_access_key="dummy",
    )

    # Verify client is configured with correct region
    assert dynamodb_client.meta.region_name == settings.aws_region
    assert dynamodb_client.meta.endpoint_url == endpoint_url
