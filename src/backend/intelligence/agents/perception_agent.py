from backend.intelligence.agents.vision_agent import VisionAgent
from backend.intelligence.graph.state import HanabnehoState


from backend.intelligence.agents.base import Agent

class PerceptionAgent(Agent):
    """
    Coordinates perception components.

    Future:
    - Vision
    - OCR
    - Speech
    """

    def __init__(self) -> None:
        self.vision = VisionAgent()

    def invoke(
        self,
        state: HanabnehoState,
    ) -> HanabnehoState:

        evidence = state["evidence"]

        if evidence.images:
            state = self.vision.invoke(state)

        return state