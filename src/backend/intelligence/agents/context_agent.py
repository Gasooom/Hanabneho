from backend.intelligence.agents.base import Agent
from backend.intelligence.graph.state import HanabnehoState


class ContextAgent(Agent):
    """
    Builds a unified EvidenceContext from all available evidence.
    """

    def invoke(
        self,
        state: HanabnehoState,
    ) -> HanabnehoState:

        evidence = state["evidence"]
        context = state["context"]

        # Preserve citizen description
        context.raw_text = evidence.text

        # Preserve GPS if available
        if evidence.latitude is not None:
            context.observations.append(
                f"Latitude: {evidence.latitude}"
            )

        if evidence.longitude is not None:
            context.observations.append(
                f"Longitude: {evidence.longitude}"
            )

        state["context"] = context

        return state