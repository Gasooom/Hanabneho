from fastapi import APIRouter, HTTPException, status

from backend.api.dependencies import report_service
from backend.schemas.api_response import ApiResponse
from backend.schemas.dashboard_report import (
    DashboardReportResponse,
)
from backend.schemas.report import (
    CreateReportRequest,
    ReportResponse,
)

router = APIRouter(
    prefix="/reports",
    tags=["Reports"],
)


@router.post(
    "",
    response_model=ApiResponse[ReportResponse],
    status_code=status.HTTP_201_CREATED,
)
def create_report(request: CreateReportRequest):
    report = report_service.create_report(request)

    return ApiResponse(
        success=True,
        message="Report created successfully.",
        data=ReportResponse.model_validate(report),
    )


@router.get(
    "",
    response_model=ApiResponse[list[ReportResponse]],
)
def list_reports():

    reports = report_service.list_reports()

    return ApiResponse(
        success=True,
        message="Reports retrieved successfully.",
        data=[
            ReportResponse.model_validate(report)
            for report in reports
        ],
    )


@router.get(
    "/dashboard",
    response_model=ApiResponse[list[DashboardReportResponse]],
)
def list_dashboard_reports():

    reports = report_service.list_dashboard_reports()

    return ApiResponse(
        success=True,
        message="Dashboard reports retrieved successfully.",
        data=reports,
    )


@router.get(
    "/{report_id}",
    response_model=ApiResponse[ReportResponse],
)
def get_report(report_id: str):

    report = report_service.get_report(report_id)

    if report is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Report not found.",
        )

    return ApiResponse(
        success=True,
        message="Report retrieved successfully.",
        data=ReportResponse.model_validate(report),
    )