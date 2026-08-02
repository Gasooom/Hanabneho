from pydantic import BaseModel, Field

from backend.schemas.api_response import ApiResponse


class AnalysisRequest(BaseModel):
    """
    Reserved for future programmatic clients.

    The current endpoint accepts multipart/form-data.
    """

    description: str


class AnalysisResponse(BaseModel):
    """
    Structured AI response.
    """

    summary: str

    category: str

    severity: str

    confidence: float

    recommended_authority: str

    reasoning: str


AnalysisApiResponse = ApiResponse[AnalysisResponse]