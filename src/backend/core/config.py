from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict

BASE_DIR = Path(__file__).resolve().parents[3]


class Settings(BaseSettings):
    # -------------------------
    # Application
    # -------------------------
    APP_NAME: str
    APP_DESCRIPTION: str
    APP_VERSION: str

    # -------------------------
    # Server
    # -------------------------
    HOST: str
    PORT: int
    DEBUG: bool

    # -------------------------
    # Logging
    # -------------------------
    LOG_LEVEL: str

    # -------------------------
    # AI
    # -------------------------
    GEMINI_API_KEY: str
    OPENAI_API_KEY: str

    # -------------------------
    # LangSmith
    # -------------------------
    LANGSMITH_API_KEY: str | None = None
    LANGSMITH_TRACING: bool = False
    LANGSMITH_PROJECT: str = "Hanabneho"

    model_config = SettingsConfigDict(
        env_file=BASE_DIR / ".env",
        case_sensitive=True,
        extra="ignore",
    )


settings = Settings()