from backend.database.base import Base
from backend.database.session import engine

# Import ORM models so SQLAlchemy registers them
from backend.database.models import AnalysisModel, ReportModel
from sqlalchemy import inspect
from sqlalchemy import text


def _ensure_created_at_column(
    table_name: str,
) -> None:

    inspector = inspect(engine)
    columns = {
        column["name"]
        for column in inspector.get_columns(table_name)
    }

    if "created_at" in columns:
        return

    with engine.begin() as connection:
        connection.execute(
            text(
                f"ALTER TABLE {table_name} ADD COLUMN created_at DATETIME"
            )
        )


def init_database() -> None:
    """
    Create all database tables if they do not already exist.
    """

    Base.metadata.create_all(bind=engine)

    for table_name in (
        "reports",
        "evidence",
        "analyses",
    ):
        _ensure_created_at_column(table_name)