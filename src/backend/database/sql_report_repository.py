from backend.database.models import AnalysisModel, EvidenceModel, ImageModel, ReportModel
from backend.database.session import SessionLocal
from backend.domain.evidence import Evidence
from backend.domain.report import Report
from backend.intelligence.models.ai_analysis import AIAnalysis
from backend.repositories.base_report_repository import (
    ReportRepository,
)
from backend.schemas.dashboard_report import (
    DashboardReportResponse,
)


class SQLReportRepository(ReportRepository):
    """
    SQLAlchemy implementation of the ReportRepository.
    """

    def save(
        self,
        report: Report,
    ) -> Report:

        with SessionLocal() as session:

            model = ReportModel(
                report_id=report.report_id,
                title=report.title,
                description=report.description,
                status=report.status,
                created_at=report.created_at,
            )

            session.add(model)
            session.commit()

        return report

    def get_by_id(
        self,
        report_id: str,
    ) -> Report | None:

        with SessionLocal() as session:

            model = session.get(
                ReportModel,
                report_id,
            )

            if model is None:
                return None

            return Report(
                report_id=model.report_id,
                title=model.title,
                description=model.description,
                status=model.status,
                created_at=model.created_at,
            )

    def list_all(
        self,
    ) -> list[Report]:

        with SessionLocal() as session:

            models = session.query(
                ReportModel
            ).all()

            return [
                Report(
                    report_id=model.report_id,
                    title=model.title,
                    description=model.description,
                    status=model.status,
                    created_at=model.created_at,
                )
                for model in models
            ]

    def list_dashboard_reports(
        self,
    ) -> list[DashboardReportResponse]:

        with SessionLocal() as session:

            rows = (
                session.query(
                    ReportModel,
                    AnalysisModel,
                )
                .join(
                    AnalysisModel,
                    ReportModel.report_id
                    == AnalysisModel.report_id,
                )
                .all()
            )

            return [
                DashboardReportResponse(
                    report_id=report.report_id,
                    title=report.title,
                    description=report.description,
                    category=analysis.category,
                    severity=analysis.severity,
                    confidence=analysis.confidence,
                    recommended_authority=analysis.recommended_authority,
                    status=report.status,
                    created_at=report.created_at,
                )
                for report, analysis in rows
            ]

    def save_analysis_bundle(
        self,
        report: Report,
        evidence: Evidence,
        analysis: AIAnalysis,
    ) -> Report:

        with SessionLocal() as session:

            report_model = ReportModel(
                report_id=report.report_id,
                title=report.title,
                description=report.description,
                status=report.status,
                created_at=report.created_at,
            )

            evidence_model = EvidenceModel(
                evidence_id=evidence.evidence_id,
                report_id=evidence.report_id,
                text=evidence.text,
                latitude=evidence.latitude,
                longitude=evidence.longitude,
                source=evidence.source,
                created_at=evidence.created_at,
            )

            analysis_model = AnalysisModel(
                report_id=report.report_id,
                summary=analysis.summary,
                category=analysis.category,
                severity=analysis.severity,
                confidence=analysis.confidence,
                recommended_authority=analysis.recommended_authority,
                reasoning=analysis.reasoning,
            )

            session.add(report_model)
            session.add(evidence_model)
            session.add(analysis_model)

            for image in evidence.images:
                session.add(
                    ImageModel(
                        evidence_id=evidence.evidence_id,
                        image_path=image.url,
                    )
                )

            session.commit()

        return report