from typing import TypedDict

from backend.domain.evidence import Evidence
from backend.intelligence.models.ai_analysis import AIAnalysis
from backend.intelligence.models.evidence_context import EvidenceContext


class HanabnehoState(TypedDict):
    """
    Shared state passed between LangGraph nodes.

    Every node reads from and writes to this object.
    """

    evidence: Evidence

    context: EvidenceContext

    analysis: AIAnalysis | None

    authority: str | None