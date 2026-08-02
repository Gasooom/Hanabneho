from dataclasses import dataclass, field


@dataclass
class EvidenceContext:
    """
    Standardized information produced from raw evidence.

    This object is gradually enriched by AI perception components
    before being sent to the reasoning engine.
    """

    raw_text: str = ""

    image_descriptions: list[str] = field(default_factory=list)

    transcript: str = ""

    ocr_text: str = ""

    location_name: str = ""

    observations: list[str] = field(default_factory=list)