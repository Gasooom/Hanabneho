from backend.database.models import ReportModel
from backend.domain.report import Report
from backend.repositories.base_report_repository import (
    ReportRepository,
)
from backend.repositories.base_sql_repository import (
    BaseSQLRepository,
)


class SQLReportRepository(
    BaseSQLRepository,
    ReportRepository,
):
    """
    SQLAlchemy implementation of the ReportRepository.

    Responsible for persisting Report domain entities while
    keeping database concerns isolated from business logic.
    """

    def save(
        self,
        report: Report,
    ) -> Report:

        with self._get_session() as session:

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

        with self._get_session() as session:

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

        with self._get_session() as session:

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