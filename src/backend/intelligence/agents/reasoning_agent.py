from backend.intelligence.agents.base import Agent
from backend.intelligence.graph.state import HanabnehoState
from backend.intelligence.reasoning.analyzer import ReasoningEngine


class ReasoningAgent(Agent):
    """
    Executes AI reasoning using the existing
    ReasoningEngine.
    """

    def __init__(self) -> None:
        self.reasoner = ReasoningEngine()

    def invoke(
        self,
        state: HanabnehoState,
    ) -> HanabnehoState:
        """
        Produce the final AIAnalysis from the
        EvidenceContext.
        """

        analysis = self.reasoner.analyze(
            state["context"],
        )

        state["analysis"] = analysis

        return state