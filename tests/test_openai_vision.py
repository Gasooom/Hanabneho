from pathlib import Path

from backend.intelligence.providers.openai_provider import OpenAIProvider


provider = OpenAIProvider()

response = provider.generate_multimodal(
    prompt="""
You are an infrastructure inspector.

Describe only what you see.

Focus on infrastructure damage,
roads,
bridges,
buildings,
public safety.

Return one concise paragraph.
""",
    image_path=Path("test_images/road.jpg"),
)

print(response)