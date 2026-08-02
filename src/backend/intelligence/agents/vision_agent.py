from backend.intelligence.agents.base import Agent
from backend.intelligence.graph.state import HanabnehoState
from backend.intelligence.perception.openai_vision import (
    OpenAIVisionProcessor,
)


class VisionAgent(Agent):
    """
    Executes image understanding using the existing
    OpenAI vision processor.
    """

    def __init__(self) -> None:
        self.processor = OpenAIVisionProcessor()

    def invoke(
        self,
        state: HanabnehoState,
    ) -> HanabnehoState:
        """
        Analyze submitted images and update the shared context.
        """

        context = self.processor.process(
            evidence=state["evidence"],
            context=state["context"],
        )

        state["context"] = context

        return state