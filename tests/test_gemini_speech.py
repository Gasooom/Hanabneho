from backend.domain.audio_evidence import AudioEvidence
from backend.domain.evidence import Evidence
from backend.intelligence.models.evidence_context import EvidenceContext
from backend.intelligence.perception.gemini_speech import (
    GeminiSpeechProcessor,
)


def test_process_adds_transcript():
    processor = GeminiSpeechProcessor()

    evidence = Evidence(
        report_id="report-1",
        audio=AudioEvidence("voice.mp3"),
    )

    context = EvidenceContext()

    updated = processor.process(evidence, context)

    assert (
        updated.transcript
        == "Mock transcript for audio: voice.mp3"
    )