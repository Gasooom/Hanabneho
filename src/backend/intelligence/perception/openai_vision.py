from pathlib import Path

from backend.domain.evidence import Evidence
from backend.intelligence.ai_gateway import AIGateway
from backend.intelligence.models.evidence_context import EvidenceContext
from backend.intelligence.perception.vision_processor import VisionProcessor


class OpenAIVisionProcessor(VisionProcessor):
    """
    Uses OpenAI Vision to enrich the EvidenceContext.
    """

    def __init__(self) -> None:
        self.gateway = AIGateway()

    def process(
        self,
        evidence: Evidence,
        context: EvidenceContext,
    ) -> EvidenceContext:

        # Preserve citizen report text
        context.raw_text = evidence.text

        prompt = (
            "You are an urban infrastructure inspection assistant.\n"
            "Describe only what is visible.\n"
            "Focus on roads, bridges, buildings, flooding, "
            "utilities, hazards and public safety.\n"
            "Return one concise paragraph."
        )

        for image in evidence.images:
            description = self.gateway.generate_multimodal(
                prompt=prompt,
                image_path=Path(image.url),
            )

            context.image_descriptions.append(description)

        return context