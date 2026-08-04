import pytest

from backend.domain.report import Report
from backend.domain.report_status import ReportStatus


def test_create_valid_report():
    report = Report(
        title="Water Pipeline Failure",
        description="Major underground water pipeline rupture causing continuous leakage and disruption to nearby neighborhoods.",
    )

    assert report.title == "Water Pipeline Failure"
    assert report.description == "Major underground water pipeline rupture causing continuous leakage and disruption to nearby neighborhoods."
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
            title="Bridge Structural Damage",
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
            title="Electrical Pole Fire",
            description="     ",
        )