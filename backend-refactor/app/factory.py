"""Application factory and configuration."""
import logging
import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from app.api.base import router as api_router
from app.api.system import router as system_router
from app.core.config import get_settings

logger = logging.getLogger(__name__)

def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()

    logger.info("Creating FastAPI application")
    logger.debug(
        "App settings loaded",
        extra={
            "app_name": settings.app_name,
            "api_version": settings.api_version,
        },
    )

    app = FastAPI(
        title=settings.app_name,
        version=settings.api_version
    )

    # The Business API
    app.include_router(api_router, prefix="/api")
    logger.debug("API router mounted at /api")

    # The System Logic
    app.include_router(system_router)
    logger.debug("System router mounted")

    # Mount the static folder using the absolute path
    current_dir = os.path.dirname(os.path.realpath(__file__))
    static_dir = os.path.join(current_dir, "static")

    if not os.path.isdir(static_dir):
        logger.warning("Static directory does not exist", extra={"path": static_dir})
    else:
        app.mount("/static", StaticFiles(directory=static_dir), name="static")
        logger.debug("Static files mounted", extra={"path": static_dir})

    return app
