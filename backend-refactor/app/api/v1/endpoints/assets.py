"""Assets endpoints (v1)."""
from typing import List
from fastapi import APIRouter, Depends, HTTPException

from app.schemas.asset import AssetResponse
from app.services.asset import AssetService

router = APIRouter()

@router.get("/", response_model=List[AssetResponse])
async def get_assets(service: AssetService = Depends()):
    """Get all assets with their signals."""
    return service.get_all_assets()
