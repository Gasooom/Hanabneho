from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.intelligence.langsmith_config import configure_langsmith
from backend.api.router import api_router
from backend.core.config import settings
from backend.core.constants import API_PREFIX
from backend.core.exceptions import register_exception_handlers
from backend.database.init_db import init_database

configure_langsmith()

app = FastAPI(
    title=settings.APP_NAME,
    description=settings.APP_DESCRIPTION,
    version=settings.APP_VERSION,
)

# ----------------------------
# CORS
# ----------------------------
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register global exception handlers
register_exception_handlers(app)


@app.get("/", tags=["Root"])
def root():
    return {
        "project": settings.APP_NAME,
        "description": settings.APP_DESCRIPTION,
        "version": settings.APP_VERSION,
        "docs": "/docs",
        "health": f"{API_PREFIX}/health",
    }


# Initialize database
init_database()

app.include_router(api_router)