from fastapi import APIRouter

from backend.utils.responses import success_response

router = APIRouter()


@router.get("/health", tags=["Health"])
def health_check():
    return success_response(
        message="Service is healthy.",
        data={
            "status": "healthy",
        },
    )


@router.get("/crash", tags=["Testing"])
def crash():
    raise Exception("Test exception")