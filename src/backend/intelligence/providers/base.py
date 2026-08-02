from abc import ABC, abstractmethod
from pathlib import Path


class LLMProvider(ABC):
    """
    Abstract base class for all LLM providers.
    """

    @abstractmethod
    def generate_text(
        self,
        prompt: str,
    ) -> str:
        """
        Generate text from a prompt.
        """
        raise NotImplementedError

    @abstractmethod
    def generate_multimodal(
        self,
        prompt: str,
        image_path: Path,
    ) -> str:
        """
        Generate a response from text and image inputs.
        """
        raise NotImplementedError