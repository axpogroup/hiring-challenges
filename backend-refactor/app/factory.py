"""Application factory and configuration."""
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from app.api.base import router as api_router
from app.api.system import router as system_router
from app.core.config import get_settings


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()

    app = FastAPI(
        title=settings.app_name,
        version=settings.api_version
    )

    # The Business API
    app.include_router(api_router, prefix="/api")

    # The System Logic
    app.include_router(system_router)

    # Mount the static folder using the absolute path
    current_dir = os.path.dirname(os.path.realpath(__file__))
    static_dir = os.path.join(current_dir, "static")
    app.mount("/static", StaticFiles(directory=static_dir), name="static")

    return app
