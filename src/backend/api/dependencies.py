from backend.repositories.report_repository import (
    InMemoryReportRepository,
)
from backend.services.analysis_service import AnalysisService
from backend.services.report_service import ReportService

# Singleton repository
report_repository = InMemoryReportRepository()

# Singleton report service
report_service = ReportService(report_repository)

# Singleton analysis service
analysis_service = AnalysisService()