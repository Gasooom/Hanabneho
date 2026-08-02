from fastapi import APIRouter

router = APIRouter()


@router.get("/authorities", tags=["Authorities"])
def get_authorities():
    return {
        "message": "Authorities endpoint",
    }