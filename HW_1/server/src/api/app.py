from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from src.api.logger import setup_uvi_loggers
from src.api.exception_handlers import (
    http_exception_handler,
    unhandled_exception_handler,
)


def create_app() -> FastAPI:
    app = FastAPI(
        openapi_url="/openapi.json",
        docs_url="/docs",
        redoc_url="/redoc",
        title="Tsirleo-app"
    )

    setup_uvi_loggers()

    from src.api.router import router

    app.include_router(router, prefix="/api/v1")

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.add_exception_handler(HTTPException, http_exception_handler)
    app.add_exception_handler(Exception, unhandled_exception_handler)

    @app.get(
        "/",
        operation_id="get_index",
    )
    async def index():
        return {"msg": "visit /docs for more info"}

    @app.get(
        "/status",
        operation_id="get_status",
    )
    async def status():
        return {"status": "healthy"}

    return app


app = create_app()
