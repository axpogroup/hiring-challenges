"""Measurement schemas."""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel

class MeasurementRequest(BaseModel):
    """Request schema for measurements endpoint."""
    signal_ids: List[str]
    from_date: datetime
    to_date: datetime

class MeasurementResponse(BaseModel):
    """Response schema for measurements."""
    signal_id: str
    timestamp: datetime
    value: float
    unit: Optional[str] = None

class MeasurementsListResponse(BaseModel):
    """List of measurements response."""
    measurements: List[MeasurementResponse]

