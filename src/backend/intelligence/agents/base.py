from abc import ABC
from abc import abstractmethod

from backend.intelligence.graph.state import HanabnehoState


class Agent(ABC):
    """
    Base contract for every AI agent in Hanabneho.
    """

    @abstractmethod
    def invoke(
        self,
        state: HanabnehoState,
    ) -> HanabnehoState:
        """
        Execute the agent and return the updated state.
        """
        raise NotImplementedError