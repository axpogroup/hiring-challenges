"""Asset schema definitions."""
from pydantic import BaseModel, Field, UUID4
from typing import List

class SignalResponse(BaseModel):
    """Schema for individual signal data."""
    id: str = Field(..., description="The internal hardware ID")
    global_id: UUID4 = Field(..., description="The unique UUID across all systems")
    name: str
    unit: str

class AssetResponse(BaseModel):
    """Schema for asset API response."""
    asset_id: str
    signals: List[SignalResponse] = []

class AssetListResponse(BaseModel):
    """Schema for list of assets."""
    assets: List[AssetResponse]

class AssetDTO(BaseModel):
    """Data transfer object for assets."""
    assetId: str
    signalData: List[dict]
