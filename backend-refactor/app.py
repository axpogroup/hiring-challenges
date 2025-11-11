"""Application factory and configuration."""
from fastapi import FastAPI
from api.v1.endpoints import assets as assets_v1
from api.v2.routes import measurements_router
from core.config import get_settings
from core.settings import AppSettings


def create_app() -> FastAPI:
    """Create and configure the FastAPI application."""
    settings = get_settings()
    app = FastAPI(
        title=settings.app_name,
        version=settings.api_version
    )
    
    # Register v1 routes
    app.include_router(assets_v1.router, prefix="/api/v1")
    app.include_router(measurements_router.router, prefix="/api/v1")
    app.include_router(assets_v1.router, tags=["assets"])
    app.include_router(measurements_router.router, tags=["measurement"])
    #app.include_router(health_check.router, prefix="/health")
    return app
