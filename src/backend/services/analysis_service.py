from backend.domain.evidence import Evidence
from backend.intelligence.graph.hanabneho_graph import HanabnehoGraph
from backend.intelligence.graph.state import HanabnehoState
from backend.intelligence.models.ai_analysis import AIAnalysis
from backend.intelligence.models.evidence_context import EvidenceContext


class AnalysisService:
    """
    High-level application service responsible for
    executing the Hanabneho AI Brain.
    """

    def __init__(self) -> None:
        self.graph = HanabnehoGraph()

    def analyze(
        self,
        evidence: Evidence,
    ) -> AIAnalysis:
        """
        Execute the LangGraph workflow and return
        the final AI analysis.
        """

        state: HanabnehoState = {
            "evidence": evidence,
            "context": EvidenceContext(),
            "analysis": None,
            "authority": None,
        }

        result = self.graph.invoke(state)

        return result["analysis"]