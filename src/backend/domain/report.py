from dataclasses import dataclass, field
from datetime import UTC, datetime
from uuid import uuid4

from backend.domain.report_status import ReportStatus


@dataclass
class Report:
    """
    Core business entity representing a citizen report.
    """

    title: str
    description: str

    report_id: str = field(default_factory=lambda: str(uuid4()))
    status: ReportStatus = ReportStatus.SUBMITTED
    created_at: datetime = field(
        default_factory=lambda: datetime.now(UTC)
    )

    def __post_init__(self) -> None:
        """
        Enforce business rules after object creation.
        """

        self.title = self.title.strip()
        self.description = self.description.strip()

        if not self.title:
            raise ValueError("Report title cannot be empty.")

        if not self.description:
            raise ValueError("Report description cannot be empty.")