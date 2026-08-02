import os

from backend.core.config import settings


def configure_langsmith() -> None:
    """
    Configure LangSmith tracing.
    """

    if not settings.LANGSMITH_API_KEY:
        return

    os.environ["LANGSMITH_API_KEY"] = settings.LANGSMITH_API_KEY
    os.environ["LANGSMITH_TRACING"] = (
        "true" if settings.LANGSMITH_TRACING else "false"
    )
    os.environ["LANGSMITH_PROJECT"] = settings.LANGSMITH_PROJECT