from dataclasses import dataclass


@dataclass(frozen=True)
class AudioEvidence:
    """
    Represents a single audio recording attached as evidence.
    """

    url: str

    def __post_init__(self) -> None:
        """
        Validate the audio URL.
        """

        if not self.url.strip():
            raise ValueError("Audio URL cannot be empty.")