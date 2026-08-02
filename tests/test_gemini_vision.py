from pathlib import Path

from backend.domain.evidence import Evidence
from backend.domain.image_evidence import ImageEvidence
from backend.intelligence.models.evidence_context import EvidenceContext
from backend.intelligence.perception.openai_vision import (
    OpenAIVisionProcessor,
)


class FakeGateway:
    def generate_multimodal(
        self,
        prompt: str,
        image_path: Path,
    ) -> str:
        return f"Description for {image_path.name}"


def test_process_adds_image_descriptions(tmp_path):
    bridge = tmp_path / "bridge.jpg"
    bridge.write_bytes(b"fake image")

    road = tmp_path / "road.jpg"
    road.write_bytes(b"fake image")

    processor = OpenAIVisionProcessor()
    processor.gateway = FakeGateway()

    evidence = Evidence(
        report_id="report-1",
        images=[
            ImageEvidence(str(bridge)),
            ImageEvidence(str(road)),
        ],
    )

    context = EvidenceContext()

    updated = processor.process(evidence, context)

    assert len(updated.image_descriptions) == 2

    assert updated.image_descriptions[0] == "Description for bridge.jpg"
    assert updated.image_descriptions[1] == "Description for road.jpg"