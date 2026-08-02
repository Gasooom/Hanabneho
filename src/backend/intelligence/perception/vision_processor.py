from abc import ABC, abstractmethod

from backend.domain.evidence import Evidence
from backend.intelligence.models.evidence_context import EvidenceContext


class VisionProcessor(ABC):
    """
    Base interface for all vision processors.

    A vision processor analyzes image evidence and enriches
    the EvidenceContext with observations.
    """

    @abstractmethod
    def process(
        self,
        evidence: Evidence,
        context: EvidenceContext,
    ) -> EvidenceContext:
        """
        Analyze image evidence and update the context.
        """
        raise NotImplementedError