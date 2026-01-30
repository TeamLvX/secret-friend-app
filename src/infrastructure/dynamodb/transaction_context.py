from contextlib import contextmanager
from typing import TYPE_CHECKING
from uuid import uuid4

from pynamodb.connection import Connection
from pynamodb.transactions import TransactWrite

from src.core.config import settings

if TYPE_CHECKING:
    from pynamodb.models import Model


class DynamoDBTransactionContext:
    """
    Transaction context using PynamoDB's native TransactWrite.
    This ensures proper serialization/deserialization of PynamoDB models.
    """

    _current_context: "DynamoDBTransactionContext | None" = None

    def __init__(self):
        self._connection = self._create_connection()
        self._transaction: TransactWrite | None = None

    @classmethod
    @contextmanager
    def begin(cls):
        context = cls()
        cls._current_context = context
        try:
            # Create a unique client request token for idempotency
            client_request_token = str(uuid4())
            with TransactWrite(connection=context._connection, client_request_token=client_request_token) as transaction:
                context._transaction = transaction
                yield context
        except Exception:
            # Transaction will be rolled back automatically by PynamoDB
            raise
        finally:
            cls._current_context = None
            context._transaction = None

    @classmethod
    def get_current(cls) -> "DynamoDBTransactionContext | None":
        return cls._current_context

    def _create_connection(self) -> Connection:
        """Create a PynamoDB Connection with proper configuration."""
        connection_kwargs = {
            "region": settings.aws_region,
        }

        if settings.dynamodb_host:
            # Local DynamoDB (for development/testing)
            connection_kwargs["host"] = settings.dynamodb_host

        if settings.aws_access_key_id:
            connection_kwargs["aws_access_key_id"] = settings.aws_access_key_id

        if settings.aws_secret_access_key:
            connection_kwargs["aws_secret_access_key"] = settings.aws_secret_access_key

        return Connection(**connection_kwargs)

    def save(self, model: "Model") -> None:
        """
        Save a PynamoDB model within the transaction.
        This uses PynamoDB's native transaction support which handles
        serialization/deserialization correctly.
        """
        if not self._transaction:
            raise RuntimeError("Transaction not started. Use 'with DynamoDBTransactionContext.begin()'")

        self._transaction.save(model)
