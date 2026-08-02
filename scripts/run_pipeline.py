from backend.domain.evidence import Evidence
from backend.domain.image_evidence import ImageEvidence
from backend.intelligence.agents.supervisor import PipelineSupervisor

supervisor = PipelineSupervisor()

evidence = Evidence(
    report_id="demo",
    text="Bridge partially collapsed after heavy rain.",
    images=[
        ImageEvidence("test_images/road.jpg"),
    ],
)

analysis = supervisor.analyze(evidence)

print("\n========== AI ANALYSIS ==========\n")

print("Summary:", analysis.summary)
print("Category:", analysis.category)
print("Severity:", analysis.severity)
print("Confidence:", analysis.confidence)
print("Recommended Authority:", analysis.recommended_authority)

print("\nReasoning:\n")
print(analysis.reasoning)