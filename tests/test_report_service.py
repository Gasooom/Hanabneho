from backend.repositories.report_repository import InMemoryReportRepository
from backend.schemas.report import CreateReportRequest
from backend.services.report_service import ReportService


def test_create_report():
    repository = InMemoryReportRepository()
    service = ReportService(repository)

    request = CreateReportRequest(
        title="Bridge Structural Damage",
        description="Visible structural cracks detected on the bridge, creating a potential safety hazard for vehicles and pedestrians.",
    )

    report = service.create_report(request)

    assert report.title == request.title
    assert report.description == request.description
    assert repository.get_by_id(report.report_id) == report


def test_get_report():
    repository = InMemoryReportRepository()
    service = ReportService(repository)

    request = CreateReportRequest(
        title="Electrical Pole Fire",
        description="Transformer fire damaged electrical infrastructure and interrupted power supply in the surrounding area.",
    )

    created_report = service.create_report(request)

    retrieved_report = service.get_report(created_report.report_id)

    assert retrieved_report == created_report


def test_list_reports():
    repository = InMemoryReportRepository()
    service = ReportService(repository)

    request1 = CreateReportRequest(
        title="Road Surface Collapse",
        description="Road surface collapsed after heavy rainfall, creating a large sinkhole that blocks traffic.",
    )

    request2 = CreateReportRequest(
        title="Flooded Drainage System",
        description="Blocked drainage system causing localized flooding and restricting access to nearby roads.",
    )

    service.create_report(request1)
    service.create_report(request2)

    reports = service.list_reports()

    assert len(reports) == 2