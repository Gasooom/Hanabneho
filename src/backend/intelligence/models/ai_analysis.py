from dataclasses import dataclass


@dataclass
class AIAnalysis:
    """
    Structured output produced by the reasoning engine.

    This object represents the AI's understanding of the
    submitted evidence.
    """

    summary: str

    category: str

    severity: str

    confidence: float

    recommended_authority: str

    reasoning: str