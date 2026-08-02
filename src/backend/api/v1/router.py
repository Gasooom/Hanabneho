from fastapi import APIRouter

from backend.api.v1.endpoints.authorities import router as authorities_router
from backend.api.v1.endpoints.health import router as health_router
from backend.api.v1.endpoints.incidents import router as incidents_router
from backend.api.v1.endpoints.reports import router as reports_router
from backend.api.v1.endpoints.analysis import (
    router as analysis_router,
)


router = APIRouter(prefix="/api/v1")

router.include_router(health_router)
router.include_router(reports_router)
router.include_router(incidents_router)
router.include_router(authorities_router)
router.include_router(analysis_router)