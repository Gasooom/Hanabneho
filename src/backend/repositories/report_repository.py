from typing import Dict

from backend.domain.evidence import Evidence
from backend.domain.report import Report
from backend.intelligence.models.ai_analysis import AIAnalysis
from backend.repositories.base_report_repository import (
    ReportRepository,
)
from backend.schemas.dashboard_report import (
    DashboardReportResponse,
)


class InMemoryReportRepository(ReportRepository):
    """
    In-memory repository used for testing and MVP.
    """

    def __init__(self) -> None:
        self._reports: Dict[str, Report] = {}
        self._evidence: Dict[str, Evidence] = {}
        self._analyses: Dict[str, AIAnalysis] = {}

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

    def list_dashboard_reports(
        self,
    ) -> list[DashboardReportResponse]:
        dashboard_reports: list[DashboardReportResponse] = []

        for report_id, report in self._reports.items():
            analysis = self._analyses.get(report_id)

            if analysis is None:
                continue

            dashboard_reports.append(
                DashboardReportResponse(
                    report_id=report.report_id,
                    title=report.title,
                    description=report.description,
                    category=analysis.category,
                    severity=analysis.severity,
                    confidence=analysis.confidence,
                    recommended_authority=analysis.recommended_authority,
                    status=report.status,
                    created_at=report.created_at,
                )
            )

        return dashboard_reports

    def save_analysis_bundle(
        self,
        report: Report,
        evidence: Evidence,
        analysis: AIAnalysis,
    ) -> Report:
        self._reports[report.report_id] = report
        self._evidence[evidence.report_id] = evidence
        self._analyses[report.report_id] = analysis

        return report