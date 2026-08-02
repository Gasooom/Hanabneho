from dataclasses import dataclass


@dataclass(frozen=True)
class ImageEvidence:
    """
    Represents a single image attached as evidence.
    """

    url: str

    def __post_init__(self) -> None:
        """
        Validate the image URL.
        """

        if not self.url.strip():
            raise ValueError("Image URL cannot be empty.")