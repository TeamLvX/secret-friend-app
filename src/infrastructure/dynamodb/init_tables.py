from src.core.config import settings
from src.infrastructure.dynamodb.models import AssignmentPynamoDB, GroupPynamoDB, ParticipantPynamoDB

TABLES = [GroupPynamoDB, AssignmentPynamoDB, ParticipantPynamoDB]


def init_tables():
    if not settings.env == "local":
        return

    for table in TABLES:
        if not table.exists():
            print(f"[LOCAL] Creating table: {table.Meta.table_name}")
            table.create_table(read_capacity_units=1, write_capacity_units=1, wait=True)


if __name__ == "__main__":
    init_tables()
