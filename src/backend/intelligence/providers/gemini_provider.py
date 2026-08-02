from pathlib import Path

from google.genai import types

from backend.intelligence.gemini_client import GeminiClient
from backend.intelligence.providers.base import LLMProvider


class GeminiProvider(LLMProvider):
    """
    Gemini implementation of the LLMProvider interface.
    """

    DEFAULT_MODEL = "gemini-2.5-flash"

    def __init__(self) -> None:
        self.client = GeminiClient().get_client()

    def generate_text(
        self,
        prompt: str,
    ) -> str:
        response = self.client.models.generate_content(
            model=self.DEFAULT_MODEL,
            contents=prompt,
            config=types.GenerateContentConfig(
                temperature=0.2,
            ),
        )

        return response.text

    def generate_multimodal(
        self,
        prompt: str,
        image_path: Path,
    ) -> str:
        """
        Generate text from an image and prompt.

        NOTE:
        This implementation is intentionally left as a placeholder
        until Gemini authentication is fully working.
        """

        raise NotImplementedError(
            "Live Gemini multimodal integration will be enabled after "
            "Gemini authentication is verified."
        )