from enum import Enum


class ReportStatus(str, Enum):
    """
    Represents the lifecycle status of a report.
    """

    DRAFT = "draft"
    SUBMITTED = "submitted"
    PROCESSING = "processing"
    ROUTED = "routed"
    ASSIGNED = "assigned"
    IN_PROGRESS = "in_progress"
    RESOLVED = "resolved"
    ARCHIVED = "archived"