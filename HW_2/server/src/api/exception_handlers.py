from fastapi import Request, status
from fastapi.exceptions import HTTPException
from fastapi.responses import JSONResponse, Response
from fastapi.utils import is_body_allowed_for_status_code
from src.api.logger import get_logger

logger = get_logger()


async def http_exception_handler(request: Request, exc: HTTPException) -> Response:
    logger.info(f"Error description: <{exc.detail}>")

    headers = getattr(exc, "headers", None)
    if not is_body_allowed_for_status_code(exc.status_code):
        return Response(status_code=exc.status_code, headers=headers)

    return JSONResponse(
        content={"detail": exc.detail},
        status_code=exc.status_code,
        headers=headers,
    )


async def unhandled_exception_handler(request: Request, exc: Exception) -> JSONResponse:
    return JSONResponse(
        content={"detail": "500 Internal Server Error: Something went wrong"},
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        headers=None,
    )
