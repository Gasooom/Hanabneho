from backend.domain.report import Report
from backend.repositories.base_report_repository import (
    ReportRepository,
)
from backend.schemas.dashboard_report import (
    DashboardReportResponse,
)
from backend.schemas.report import CreateReportRequest


class ReportService:
    """
    Handles report-related business operations.
    """

    def __init__(
        self,
        repository: ReportRepository,
    ) -> None:
        self.repository = repository

    def create_report(
        self,
        request: CreateReportRequest,
    ) -> Report:

        report = Report(
            title=request.title,
            description=request.description,
        )

        return self.repository.save(report)

    def get_report(
        self,
        report_id: str,
    ) -> Report | None:

        return self.repository.get_by_id(report_id)

    def list_reports(
        self,
    ) -> list[Report]:

        return self.repository.list_all()

    def list_dashboard_reports(
        self,
    ) -> list[DashboardReportResponse]:

        return self.repository.list_dashboard_reports()