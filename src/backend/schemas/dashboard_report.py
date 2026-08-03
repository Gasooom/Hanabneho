from datetime import datetime

from pydantic import BaseModel, ConfigDict

from backend.domain.report_status import ReportStatus


class DashboardReportResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    report_id: str
    title: str
    description: str

    category: str
    severity: str
    confidence: float
    recommended_authority: str

    status: ReportStatus
    created_at: datetime