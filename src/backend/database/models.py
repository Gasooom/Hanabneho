from datetime import UTC, datetime
from uuid import uuid4

from sqlalchemy import DateTime
from sqlalchemy import Enum
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

from backend.database.base import Base
from backend.domain.evidence_source import EvidenceSource
from backend.domain.report_status import ReportStatus


class ReportModel(Base):
    """
    Database representation of a citizen report.
    """

    __tablename__ = "reports"

    report_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    title: Mapped[str] = mapped_column(
        String(150),
        nullable=False,
    )

    description: Mapped[str] = mapped_column(
        String(2000),
        nullable=False,
    )

    status: Mapped[ReportStatus] = mapped_column(
        Enum(ReportStatus),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    evidence: Mapped["EvidenceModel"] = relationship(
        back_populates="report",
        cascade="all, delete-orphan",
        uselist=False,
    )

    analysis: Mapped["AnalysisModel"] = relationship(
        back_populates="report",
        cascade="all, delete-orphan",
        uselist=False,
    )


class EvidenceModel(Base):
    """
    Raw evidence submitted with a report.
    """

    __tablename__ = "evidence"

    evidence_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    report_id: Mapped[str] = mapped_column(
        ForeignKey("reports.report_id"),
        unique=True,
    )

    text: Mapped[str] = mapped_column(
        String(5000),
        default="",
    )

    latitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    longitude: Mapped[float | None] = mapped_column(
        Float,
        nullable=True,
    )

    source: Mapped[EvidenceSource] = mapped_column(
        Enum(EvidenceSource),
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    report: Mapped["ReportModel"] = relationship(
        back_populates="evidence",
    )

    images: Mapped[list["ImageModel"]] = relationship(
        back_populates="evidence",
        cascade="all, delete-orphan",
    )


class ImageModel(Base):
    """
    Image attached to evidence.
    """

    __tablename__ = "images"

    image_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    evidence_id: Mapped[str] = mapped_column(
        ForeignKey("evidence.evidence_id"),
    )

    image_path: Mapped[str] = mapped_column(
        String(1000),
        nullable=False,
    )

    evidence: Mapped["EvidenceModel"] = relationship(
        back_populates="images",
    )


class AnalysisModel(Base):
    """
    AI analysis generated from report evidence.
    """

    __tablename__ = "analyses"

    analysis_id: Mapped[str] = mapped_column(
        String(36),
        primary_key=True,
        default=lambda: str(uuid4()),
    )

    report_id: Mapped[str] = mapped_column(
        ForeignKey("reports.report_id"),
        unique=True,
    )

    summary: Mapped[str] = mapped_column(
        String(2000),
    )

    category: Mapped[str] = mapped_column(
        String(100),
    )

    severity: Mapped[str] = mapped_column(
        String(50),
    )

    confidence: Mapped[float] = mapped_column(
        Float,
    )

    recommended_authority: Mapped[str] = mapped_column(
        String(255),
    )

    reasoning: Mapped[str] = mapped_column(
        String(5000),
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(UTC),
    )

    report: Mapped["ReportModel"] = relationship(
        back_populates="analysis",
    )