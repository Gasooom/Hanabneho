from typing import TypeVar

from backend.schemas.api_response import ApiResponse
from backend.schemas.error_response import ErrorResponse

T = TypeVar("T")


def success_response(
    message: str,
    data: T | None = None,
) -> ApiResponse[T]:
    return ApiResponse(
        success=True,
        message=message,
        data=data,
    )


def error_response(
    message: str,
    errors: list[str] | None = None,
) -> ErrorResponse:
    return ErrorResponse(
        message=message,
        errors=errors or [],
    )