from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4

from backend.domain.audio_evidence import AudioEvidence
from backend.domain.evidence_source import EvidenceSource
from backend.domain.image_evidence import ImageEvidence


@dataclass
class Evidence:
    """
    Represents the raw evidence attached to a report.
    """

    report_id: str

    text: str = ""

    images: list[ImageEvidence] = field(default_factory=list)

    audio: AudioEvidence | None = None

    latitude: float | None = None
    longitude: float | None = None

    source: EvidenceSource = EvidenceSource.CITIZEN

    evidence_id: str = field(default_factory=lambda: str(uuid4()))

    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def __post_init__(self) -> None:
        """
        Normalize text.
        """

        self.text = self.text.strip()