import json

from backend.intelligence.agents.prompts.reasoning import SYSTEM_PROMPT
from backend.intelligence.ai_gateway import AIGateway
from backend.intelligence.models.ai_analysis import AIAnalysis
from backend.intelligence.models.evidence_context import EvidenceContext


class ReasoningEngine:

    def __init__(self) -> None:
        self.gateway = AIGateway()

    def analyze(
        self,
        context: EvidenceContext,
    ) -> AIAnalysis:

        evidence = f"""
Citizen Report:
{context.raw_text}

Image Analysis:
{chr(10).join(context.image_descriptions)}

Speech:
{context.transcript}

OCR:
{context.ocr_text}

Observations:
{chr(10).join(context.observations)}
"""

        response = self.gateway.generate_text(
            f"{SYSTEM_PROMPT}\n\n{evidence}"
        )

        data = json.loads(response)

        return AIAnalysis(
            summary=data["summary"],
            category=data["category"],
            severity=data["severity"],
            confidence=float(data["confidence"]),
            recommended_authority=data["recommended_authority"],
            reasoning=data["reasoning"],
        )