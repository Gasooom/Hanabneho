from backend.domain.evidence import Evidence
from backend.domain.image_evidence import ImageEvidence
from backend.intelligence.graph.hanabneho_graph import HanabnehoGraph
from backend.intelligence.graph.state import HanabnehoState
from backend.intelligence.models.evidence_context import EvidenceContext

graph = HanabnehoGraph()

state: HanabnehoState = {
    "evidence": Evidence(
        report_id="demo",
        text="Bridge collapsed after heavy rain.",
        images=[
            ImageEvidence("test_images/road.jpg"),
        ],
    ),
    "context": EvidenceContext(),
    "analysis": None,
    "authority": None,
}

result = graph.invoke(state)

analysis = result["analysis"]

print("\nAuthority:")
print(result["authority"])

print("\n========== AI ANALYSIS ==========\n")

print("Summary:", analysis.summary)
print("Category:", analysis.category)
print("Severity:", analysis.severity)
print("Confidence:", analysis.confidence)
print("Recommended Authority:", analysis.recommended_authority)

print("\nReasoning:\n")
print(analysis.reasoning)