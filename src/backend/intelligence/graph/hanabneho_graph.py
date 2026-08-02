from langgraph.graph import END
from langgraph.graph import START
from langgraph.graph import StateGraph

from backend.intelligence.agents.context_agent import ContextAgent
from backend.intelligence.agents.perception_agent import PerceptionAgent
from backend.intelligence.agents.reasoning_agent import ReasoningAgent
from backend.intelligence.agents.routing_agent import RoutingAgent
from backend.intelligence.agents.supervisor_agent import SupervisorAgent
from backend.intelligence.graph.state import HanabnehoState


class HanabnehoGraph:

    def __init__(self):

        self.supervisor = SupervisorAgent()
        self.perception = PerceptionAgent()
        self.context = ContextAgent()
        self.reasoning = ReasoningAgent()
        self.routing = RoutingAgent()

        workflow = StateGraph(HanabnehoState)

        workflow.add_node(
            "supervisor",
            self.supervisor.invoke,
        )

        workflow.add_node(
            "perception",
            self.perception.invoke,
        )

        workflow.add_node(
            "context",
            self.context.invoke,
        )

        workflow.add_node(
            "reasoning",
            self.reasoning.invoke,
        )

        workflow.add_node(
            "routing",
            self.routing.invoke,
        )

        workflow.add_edge(
            START,
            "supervisor",
        )

        workflow.add_edge(
            "supervisor",
            "perception",
        )

        workflow.add_edge(
            "perception",
            "context",
        )

        workflow.add_edge(
            "context",
            "reasoning",
        )

        workflow.add_edge(
            "reasoning",
            "routing",
        )

        workflow.add_edge(
            "routing",
            END,
        )

        self.graph = workflow.compile()

    def invoke(self, state):
        return self.graph.invoke(state)