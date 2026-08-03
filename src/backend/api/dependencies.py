from backend.database.sql_report_repository import (
    SQLReportRepository,
)
from backend.services.analysis_service import AnalysisService
from backend.services.report_service import ReportService

# Singleton repository (SQLite)
report_repository = SQLReportRepository()

# Singleton report service
report_service = ReportService(report_repository)

# Singleton analysis service
analysis_service = AnalysisService()