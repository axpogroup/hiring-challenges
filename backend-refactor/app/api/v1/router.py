"""Base router for API v1 endpoints."""
from fastapi import APIRouter
from app.api.v1.endpoints import assets, measurements

router = APIRouter()

router.include_router(assets.router, prefix="/assets", tags=["Assets"])

router.include_router(measurements.router, prefix="/measurements", tags=["Measurements"])
