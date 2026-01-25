"""Asset model definition."""
from typing import List, Optional
from pydantic import BaseModel

class AssetModel(BaseModel):
    """Asset model with signals."""
    asset_id: str
    signals: List[dict]

class Asset(BaseModel):
    """Alternative Asset representation."""
    assetId: str
    signalList: List[dict]

def create_asset(asset_id: str, signals: list) -> AssetModel:
    """Factory function to create asset."""
    return AssetModel(asset_id=asset_id, signals=signals)
