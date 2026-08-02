import pytest

from backend.domain.report import Report
from backend.domain.report_status import ReportStatus


def test_create_valid_report():
    report = Report(
        title="Broken Water Pipe",
        description="A large water leak near the primary school.",
    )

    assert report.title == "Broken Water Pipe"
    assert report.description == "A large water leak near the primary school."
    assert report.status == ReportStatus.SUBMITTED
    assert report.report_id is not None
    assert report.created_at is not None


def test_empty_title_raises_error():
    with pytest.raises(ValueError):
        Report(
            title="",
            description="Water leak",
        )


def test_empty_description_raises_error():
    with pytest.raises(ValueError):
        Report(
            title="Broken Pipe",
            description="",
        )


def test_whitespace_title_raises_error():
    with pytest.raises(ValueError):
        Report(
            title="   ",
            description="Water leak",
        )


def test_whitespace_description_raises_error():
    with pytest.raises(ValueError):
        Report(
            title="Broken Pipe",
            description="     ",
        )