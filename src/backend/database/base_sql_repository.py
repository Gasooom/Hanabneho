from sqlalchemy.orm import Session

from backend.database.session import SessionLocal


class BaseSQLRepository:
    """
    Base class for SQLAlchemy repositories.

    Provides a consistent way to execute database operations
    using managed SQLAlchemy sessions.
    """

    def __init__(self) -> None:
        self._session_factory = SessionLocal

    def _get_session(self) -> Session:
        """
        Create a new database session.

        Returns:
            Session: SQLAlchemy session.
        """
        return self._session_factory()