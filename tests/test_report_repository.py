from backend.domain.report import Report
from backend.repositories.report_repository import InMemoryReportRepository


def test_save_report():
    repository = InMemoryReportRepository()

    report = Report(
        title="Water Pipeline Failure",
        description="Major underground water pipeline rupture causing continuous leakage and disruption to nearby neighborhoods.",
    )

    saved_report = repository.save(report)

    assert saved_report == report
    assert saved_report.report_id == report.report_id


def test_get_report_by_id():
    repository = InMemoryReportRepository()

    report = Report(
        title="Electrical Pole Fire",
        description="Transformer fire damaged electrical infrastructure and interrupted power supply in the surrounding area.",
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
        title="Flooded Drainage System",
        description="Blocked drainage system causing localized flooding and restricting access to nearby roads.",
    )

    report2 = Report(
        title="Road Surface Collapse",
        description="Road surface collapsed after heavy rainfall, creating a large sinkhole that blocks traffic.",
    )

    repository.save(report1)
    repository.save(report2)

    reports = repository.list_all()

    assert len(reports) == 2
    assert report1 in reports
    assert report2 in reports