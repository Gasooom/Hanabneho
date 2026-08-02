from fastapi import APIRouter

router = APIRouter()


@router.get("/incidents", tags=["Incidents"])
def get_incidents():
    return {
        "message": "Incidents endpoint",
    }