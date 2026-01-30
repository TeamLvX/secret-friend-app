from src.core.config import settings
from src.infrastructure.dynamodb.models import AssignmentPynamoDB, GroupPynamoDB, ParticipantPynamoDB

TABLES = [GroupPynamoDB, AssignmentPynamoDB, ParticipantPynamoDB]


def init_tables():
    """Initialize DynamoDB tables for local development."""
    # Only create tables in local/development environment
    if settings.env not in ("local", "development"):
        print(f"[SKIP] Skipping table creation for environment: {settings.env}")
        return

    print(f"[INIT] Initializing DynamoDB tables for environment: {settings.env}")
    for table in TABLES:
        if not table.exists():
            print(f"[LOCAL] Creating table: {table.Meta.table_name}")
            table.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)
        else:
            print(f"[LOCAL] Table already exists: {table.Meta.table_name}")


if __name__ == "__main__":
    init_tables()
