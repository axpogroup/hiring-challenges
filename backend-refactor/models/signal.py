"""Signal model definitions."""
from typing import Optional
from pydantic import BaseModel

class SignalModel(BaseModel):
    """Signal model."""
    SignalGId: str
    SignalId: str
    SignalName: str
    AssetId: str
    Unit: str

class Signal(BaseModel):
    """Alternative signal representation."""
    signal_gid: str
    signal_id: str
    signal_name: str
    asset_id: str
    unit: str

class signal_dto(BaseModel):
    """Yet another signal representation (camelCase)."""
    signalGId: str
    signalId: str
    signalName: str
    assetId: str
    unit: str
