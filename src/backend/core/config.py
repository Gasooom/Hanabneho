from pydantic_settings import BaseSettings, SettingsConfigDict


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

    model_config = SettingsConfigDict(
        env_file=".env",
        case_sensitive=True,
    )


settings = Settings()