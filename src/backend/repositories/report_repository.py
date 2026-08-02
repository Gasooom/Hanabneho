from typing import Dict

from backend.domain.report import Report
from backend.repositories.base_report_repository import (
    ReportRepository,
)


class InMemoryReportRepository(ReportRepository):
    """
    In-memory repository used for testing and MVP.
    """

    def __init__(self) -> None:
        self._reports: Dict[str, Report] = {}

    def save(
        self,
        report: Report,
    ) -> Report:
        self._reports[report.report_id] = report
        return report

    def get_by_id(
        self,
        report_id: str,
    ) -> Report | None:
        return self._reports.get(report_id)

    def list_all(
        self,
    ) -> list[Report]:
        return list(self._reports.values())