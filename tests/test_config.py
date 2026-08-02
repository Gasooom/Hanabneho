from backend.core.config import settings


def test_settings():
    assert settings.APP_NAME == "Hanabneho API"
    assert settings.APP_VERSION == "0.1.0"
    assert settings.HOST == "127.0.0.1"
    assert settings.PORT == 8000
    assert settings.DEBUG is True
    assert settings.LOG_LEVEL == "INFO"