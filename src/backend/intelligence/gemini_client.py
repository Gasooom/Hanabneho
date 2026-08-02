from google import genai

from backend.core.config import settings


class GeminiClient:
    """
    Provides a shared Gemini client for the Intelligence Engine.
    """

    def __init__(self) -> None:
        self.client = genai.Client(
            api_key=settings.GEMINI_API_KEY,
        )

    def get_client(self) -> genai.Client:
        """
        Return the initialized Gemini client.
        """
        return self.client