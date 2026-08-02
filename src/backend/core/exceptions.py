from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from backend.utils.responses import error_response


def register_exception_handlers(app: FastAPI) -> None:
    @app.exception_handler(Exception)
    async def global_exception_handler(
        request: Request,
        exc: Exception,
    ) -> JSONResponse:
        response = error_response(
            message="An unexpected error occurred.",
            errors=[str(exc)],
        )

        return JSONResponse(
            status_code=500,
            content=response.model_dump(),
        )