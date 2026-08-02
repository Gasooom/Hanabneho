from backend.domain.report import Report
from backend.repositories.base_report_repository import (
    ReportRepository,
)
from backend.schemas.report import CreateReportRequest


class ReportService:
    """
    Handles report-related business operations.

    The service depends on the repository abstraction rather than
    a concrete implementation. This allows different persistence
    strategies (in-memory, SQLite, PostgreSQL, etc.) without
    modifying business logic.
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
        """
        Create a new report and persist it.
        """

        report = Report(
            title=request.title,
            description=request.description,
        )

        return self.repository.save(report)

    def get_report(
        self,
        report_id: str,
    ) -> Report | None:
        """
        Retrieve a report by its unique identifier.
        """

        return self.repository.get_by_id(report_id)

    def list_reports(
        self,
    ) -> list[Report]:
        """
        Retrieve all stored reports.
        """

        return self.repository.list_all()