from backend.domain.report import Report
from backend.repositories.report_repository import InMemoryReportRepository


def test_save_report():
    repository = InMemoryReportRepository()

    report = Report(
        title="Broken Water Pipe",
        description="Large water leak near the primary school.",
    )

    saved_report = repository.save(report)

    assert saved_report == report
    assert saved_report.report_id == report.report_id


def test_get_report_by_id():
    repository = InMemoryReportRepository()

    report = Report(
        title="Power Outage",
        description="Electricity has been down for two hours.",
    )

    repository.save(report)

    retrieved_report = repository.get_by_id(report.report_id)

    assert retrieved_report == report


def test_get_unknown_report_returns_none():
    repository = InMemoryReportRepository()

    report = repository.get_by_id("unknown-id")

    assert report is None


def test_list_all_reports():
    repository = InMemoryReportRepository()

    report1 = Report(
        title="Broken Water Pipe",
        description="Large water leak.",
    )

    report2 = Report(
        title="Road Damage",
        description="Large pothole on the main road.",
    )

    repository.save(report1)
    repository.save(report2)

    reports = repository.list_all()

    assert len(reports) == 2
    assert report1 in reports
    assert report2 in reports