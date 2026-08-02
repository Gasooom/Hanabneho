from backend.intelligence.models.ai_analysis import AIAnalysis
from backend.intelligence.models.evidence_context import EvidenceContext


class WorkingMemory:
    """
    Stores the current reasoning state during an AI workflow.

    This is short-term memory. It exists only for the lifetime
    of a single report analysis.
    """

    def __init__(self) -> None:
        self.context: EvidenceContext | None = None
        self.analysis: AIAnalysis | None = None

    def remember_context(
        self,
        context: EvidenceContext,
    ) -> None:
        self.context = context

    def remember_analysis(
        self,
        analysis: AIAnalysis,
    ) -> None:
        self.analysis = analysis

    def get_context(self) -> EvidenceContext | None:
        return self.context

    def get_analysis(self) -> AIAnalysis | None:
        return self.analysis

    def clear(self) -> None:
        self.context = None
        self.analysis = None