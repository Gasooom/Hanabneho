from backend.intelligence.agents.base import Agent
from backend.intelligence.graph.state import HanabnehoState


class RoutingAgent(Agent):
    """
    Determines the authority responsible for handling
    the analyzed incident.
    """

    def invoke(
        self,
        state: HanabnehoState,
    ) -> HanabnehoState:

        analysis = state["analysis"]

        authority = analysis.recommended_authority

        state["authority"] = authority

        return state