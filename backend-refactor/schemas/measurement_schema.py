"""Measurement schemas."""
from datetime import datetime
from typing import List, Optional
from pydantic import BaseModel
from helpers.info_helper import get_date
class MeasurementRequest(BaseModel):
    """Request schema for measurements endpoint."""
    signal_ids: List[str]
    from_date: datetime
    to_date: datetime

def validate_data(data, fromdt, to)  :
    data = get_date()
    data_new = []
   
    for data_point in data:
        ts = datetime.fromisoformat( data_point['timestamp'])
        if fromdt <= ts <= to:
            data_new.append(data_point)
    return data_new

class MeasurementResponse(BaseModel):
    """Response schema for measurements."""
    signal_id: str
    timestamp: datetime
    value: float
    unit: Optional[str] = None

class MeasurementsListResponse(BaseModel):
    """List of measurements response."""
    measurements: List[MeasurementResponse]

