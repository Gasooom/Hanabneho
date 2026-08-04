from pathlib import Path
from tempfile import NamedTemporaryFile

from fastapi import APIRouter, File, Form, UploadFile

from backend.api.dependencies import analysis_service, report_service
from backend.domain.evidence import Evidence
from backend.domain.image_evidence import ImageEvidence
from backend.domain.report import Report
from backend.schemas.analysis import (
    AnalysisApiResponse,
    AnalysisResponse,
)


def _build_report_title(
    description: str,
    filename: str | None,
) -> str:

    normalized_description = " ".join(description.split()).strip()

    if normalized_description:
        return normalized_description.splitlines()[0][:150]

    filename_stem = Path(filename or "").stem.replace("_", " ").replace("-", " ").strip()

    return filename_stem[:150]

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

    suffix = Path(image.filename or "").suffix or ".jpg"

    with NamedTemporaryFile(
        delete=False,
        suffix=suffix,
    ) as temp:
        temp.write(await image.read())
        temp_path = Path(temp.name)

    report_title = _build_report_title(
        description=description,
        filename=image.filename,
    )

    normalized_description = " ".join(description.split()).strip()

    report = Report(
        title=report_title,
        description=normalized_description or report_title,
    )

    evidence = Evidence(
        report_id=report.report_id,
        text=normalized_description,
        images=[
            ImageEvidence(
                url=str(temp_path)
            )
        ],
    )

    analysis = analysis_service.analyze(
        evidence
    )

    report_service.repository.save_analysis_bundle(
        report=report,
        evidence=evidence,
        analysis=analysis,
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