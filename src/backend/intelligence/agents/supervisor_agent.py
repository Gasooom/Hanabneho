from backend.intelligence.agents.base import Agent
from backend.intelligence.graph.state import HanabnehoState


class SupervisorAgent(Agent):
    """
    Entry point of the Hanabneho AI Brain.

    The supervisor validates the shared state and
    delegates execution to downstream agents.
    """

    def invoke(
        self,
        state: HanabnehoState,
    ) -> HanabnehoState:
        """
        Validate the incoming graph state.
        """

        if state.get("evidence") is None:
            raise ValueError(
                "Graph state is missing evidence."
            )

        if state.get("context") is None:
            raise ValueError(
                "Graph state is missing context."
            )

        return state