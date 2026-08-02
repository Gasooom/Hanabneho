from pathlib import Path

from backend.intelligence.providers.base import LLMProvider
from backend.intelligence.providers.openai_provider import OpenAIProvider


class AIGateway:
    """
    Central gateway for all LLM interactions.
    """

    def __init__(
        self,
        provider: LLMProvider | None = None,
    ) -> None:
        self.provider = provider or OpenAIProvider()

    def generate_text(
        self,
        prompt: str,
    ) -> str:
        """
        Generate text using the configured provider.
        """
        return self.provider.generate_text(prompt)

    def generate_multimodal(
        self,
        prompt: str,
        image_path: Path,
    ) -> str:
        """
        Generate a response from text and image inputs.

        This delegates the implementation to the configured provider.
        """
        return self.provider.generate_multimodal(
            prompt=prompt,
            image_path=image_path,
        )