from fastapi import FastAPI
from fastapi.responses import UJSONResponse

from routers.router import api_router


def get_app() -> FastAPI:
    app = FastAPI(
        title="JanBot",
        version="V.0.1",
        docs_url="/api/docs",
        redoc_url="/api/redoc",
        openapi_url="/api/openapi.json",
        default_response_class=UJSONResponse
    )

    app.include_router(router=api_router, prefix="/api")

    return app
