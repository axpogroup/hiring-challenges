"""Assets endpoint (v1)."""
from typing import List
from fastapi import APIRouter, Depends, HTTPException
from app.services.asset_service import AssetService
from app.schemas.asset_schema import AssetResponse
from app.utils.helpers import validate_data

router = APIRouter()

@router.get("/", response_model=List[AssetResponse])
async def get_assets(service: AssetService = Depends()):
    """Get all assets with their signals."""
    try:
        assets = service.get_all_assets()
        
        if not validate_data(assets):
            raise HTTPException(status_code=404, detail="No assets found")
        
        return assets
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
