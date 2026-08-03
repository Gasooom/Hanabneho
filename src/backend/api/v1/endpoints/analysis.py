from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import APIRouter, File, Form, UploadFile

from backend.api.dependencies import analysis_service
from backend.domain.evidence import Evidence
from backend.domain.image_evidence import ImageEvidence
from backend.schemas.analysis import (
    AnalysisApiResponse,
    AnalysisResponse,
)

router = APIRouter(
    prefix="/reports",
    tags=["AI Analysis"],
)


@router.post(
    "/analyze",
    response_model=AnalysisApiResponse,
)
async def analyze_report(
    description: str = Form(""),
    image: UploadFile = File(...),
):
    """
    Analyze uploaded infrastructure evidence.
    """

    suffix = Path(image.filename).suffix or ".jpg"

    with NamedTemporaryFile(
        delete=False,
        suffix=suffix,
    ) as temp:
        temp.write(await image.read())
        temp_path = Path(temp.name)

    try:
        evidence = Evidence(
            report_id="manual-analysis",
            text=description,
            images=[
                ImageEvidence(
                    url=str(temp_path)
                )
            ],
        )

        analysis = analysis_service.analyze(
            evidence
        )

        return AnalysisApiResponse(
            success=True,
            message="Analysis completed successfully.",
            data=AnalysisResponse(
                summary=analysis.summary,
                category=analysis.category,
                severity=analysis.severity,
                confidence=analysis.confidence,
                recommended_authority=analysis.recommended_authority,
                reasoning=analysis.reasoning,
            ),
        )

    finally:
        if temp_path.exists():
            temp_path.unlink()