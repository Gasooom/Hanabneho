from abc import ABC, abstractmethod

from backend.domain.report import Report


class ReportRepository(ABC):
    """
    Abstract repository for Report entities.
    """

    @abstractmethod
    def save(
        self,
        report: Report,
    ) -> Report:
        raise NotImplementedError

    @abstractmethod
    def get_by_id(
        self,
        report_id: str,
    ) -> Report | None:
        raise NotImplementedError

    @abstractmethod
    def list_all(
        self,
    ) -> list[Report]:
        raise NotImplementedError