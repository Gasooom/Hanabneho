from backend.database.base import Base
from backend.database.session import engine

# Import ORM models so SQLAlchemy registers them
from backend.database.models import AnalysisModel, ReportModel


def init_database() -> None:
    """
    Create all database tables if they do not already exist.
    """

    Base.metadata.create_all(bind=engine)