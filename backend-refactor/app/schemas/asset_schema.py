"""Asset schema definitions."""
from typing import List
from pydantic import BaseModel

class AssetResponse(BaseModel):
    """Schema for asset API response."""
    asset_id: str
    signals: List[dict]

class AssetListResponse(BaseModel):
    """Schema for list of assets."""
    assets: List[AssetResponse]

class AssetDTO(BaseModel):
    """Data transfer object for assets."""
    assetId: str
    signalData: List[dict]
