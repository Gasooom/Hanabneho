from base64 import b64encode
from pathlib import Path

from openai import OpenAI

from backend.core.config import settings
from backend.intelligence.providers.base import LLMProvider


class OpenAIProvider(LLMProvider):
    """
    OpenAI implementation of the LLMProvider interface.
    """

    DEFAULT_MODEL = "gpt-4.1-mini"

    def __init__(self) -> None:
        self.client = OpenAI(api_key=settings.OPENAI_API_KEY)

    def generate_text(
        self,
        prompt: str,
    ) -> str:
        response = self.client.responses.create(
            model=self.DEFAULT_MODEL,
            input=prompt,
        )

        return response.output_text

    def generate_multimodal(
        self,
        prompt: str,
        image_path: Path,
    ) -> str:
        image_bytes = image_path.read_bytes()
        image_base64 = b64encode(image_bytes).decode("utf-8")

        response = self.client.responses.create(
            model=self.DEFAULT_MODEL,
            input=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": prompt,
                        },
                        {
                            "type": "input_image",
                            "image_url": f"data:image/jpeg;base64,{image_base64}",
                        },
                    ],
                }
            ],
        )

        return response.output_text