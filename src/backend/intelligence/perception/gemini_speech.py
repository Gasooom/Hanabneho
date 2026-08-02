from backend.domain.evidence import Evidence
from backend.intelligence.models.evidence_context import EvidenceContext


class GeminiSpeechProcessor:
    """
    Mock implementation of the speech perception component.

    In the MVP, this class simulates speech-to-text.
    Later, it will use the Gemini API to transcribe audio.
    """

    def process(
        self,
        evidence: Evidence,
        context: EvidenceContext,
    ) -> EvidenceContext:
        """
        Analyze audio evidence and enrich the EvidenceContext.
        """

        if evidence.audio is not None:
            context.transcript = (
                f"Mock transcript for audio: {evidence.audio.url}"
            )

        return context