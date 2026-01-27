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

class MeasurementStatsResponse(BaseModel):
    """Response schema for measurement stats."""
    signal_id: str
    from_date: datetime
    to_date: datetime
    count: int
    mean: Optional[float] = None
    min: Optional[float] = None
    max: Optional[float] = None
    median: Optional[float] = None
    std_dev: Optional[float] = None
