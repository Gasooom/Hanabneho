from datetime import datetime
from uuid import UUID

from pydantic import BaseModel, ConfigDict, Field

from backend.domain.report_status import ReportStatus


class CreateReportRequest(BaseModel):
    """
    Request schema for creating a new report.
    """

    title: str = Field(
        ...,
        min_length=5,
        max_length=150,
        description="Short title describing the incident.",
        examples=["Water Pipeline Failure"],
    )

    description: str = Field(
        ...,
        min_length=10,
        max_length=2000,
        description="Detailed description of the incident.",
        examples=[
            "Major underground water pipeline rupture causing continuous leakage and disruption to nearby neighborhoods.",
        ],
    )


class ReportResponse(BaseModel):
    """
    Response schema returned after creating or retrieving a report.
    """

    report_id: UUID
    title: str
    description: str
    status: ReportStatus
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)