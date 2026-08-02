from backend.repositories.report_repository import InMemoryReportRepository
from backend.schemas.report import CreateReportRequest
from backend.services.report_service import ReportService


def test_create_report():
    repository = InMemoryReportRepository()
    service = ReportService(repository)

    request = CreateReportRequest(
        title="Broken Water Pipe",
        description="Large water leak near the primary school.",
    )

    report = service.create_report(request)

    assert report.title == request.title
    assert report.description == request.description
    assert repository.get_by_id(report.report_id) == report


def test_get_report():
    repository = InMemoryReportRepository()
    service = ReportService(repository)

    request = CreateReportRequest(
        title="Power Outage",
        description="Electricity has been down for two hours.",
    )

    created_report = service.create_report(request)

    retrieved_report = service.get_report(created_report.report_id)

    assert retrieved_report == created_report


def test_list_reports():
    repository = InMemoryReportRepository()
    service = ReportService(repository)

    request1 = CreateReportRequest(
        title="Road Damage",
        description="Large pothole on the main road.",
    )

    request2 = CreateReportRequest(
        title="Street Light",
        description="Street light has stopped working.",
    )

    service.create_report(request1)
    service.create_report(request2)

    reports = service.list_reports()

    assert len(reports) == 2