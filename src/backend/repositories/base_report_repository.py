from abc import ABC, abstractmethod

from backend.domain.evidence import Evidence
from backend.domain.report import Report
from backend.intelligence.models.ai_analysis import AIAnalysis
from backend.schemas.dashboard_report import (
    DashboardReportResponse,
)


class ReportRepository(ABC):
    """
    Abstract repository for Report entities.
    """

    @abstractmethod
    def save(
        self,
        report: Report,
    ) -> Report:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(
        self,
        report_id: str,
    ) -> Report | None:
        raise NotImplementedError

    @abstractmethod
    def list_all(
        self,
    ) -> list[Report]:
        raise NotImplementedError

    @abstractmethod
    def list_dashboard_reports(
        self,
    ) -> list[DashboardReportResponse]:
        raise NotImplementedError

    @abstractmethod
    def save_analysis_bundle(
        self,
        report: Report,
        evidence: Evidence,
        analysis: AIAnalysis,
    ) -> Report:
        raise NotImplementedError