"""Measurements endpoints (v1)"""
from fastapi import APIRouter, HTTPException, Query, Depends
from typing import Any, List, Optional, Dict
from datetime import datetime
from app.services.measurement import MeasurementService
from app.schemas.measurement import MeasurementResponse
from app.utils.date_utils import parse_date, validate_date_range

router = APIRouter()

measurement_service = MeasurementService()

@router.get("/", response_model=List[MeasurementResponse])
async def get_measurements(
    signalIds: str = Query(..., description="Comma-separated signal IDs"),
    from_date: str = Query(..., alias="from", description="Start date (ISO format)"),
    to_date: str = Query(..., alias="to", description="End date (ISO format)"),
    service: MeasurementService = Depends()
):
    """Get measurements for specified signals and date range."""
    try:
        signal_id_list = [sid.strip() for sid in signalIds.split(",")]
        from_dt = parse_date(from_date)
        to_dt = parse_date(to_date)

        return service.get_measurements(signal_id_list, from_dt, to_dt)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid date format: {str(e)}")

@router.get("/stats/{signal_id}", response_model=Any)
async def get_signal_stats(
    signal_id: str,
    from_date: str = Query(..., alias="from", description="Start date (ISO format)"),
    to_date: str = Query(..., alias="to", description="End date (ISO format)")
):
    """Calculate statistics for a signal over a date range.
    
    Returns:
        - count: Number of measurements
        - mean: Average value
        - min: Minimum value
        - max: Maximum value
        - median: Median value
        - std_dev: Standard deviation
    """
    try:
        from_dt = datetime.fromisoformat(from_date)
        to_dt = datetime.fromisoformat(to_date)
        
        stats = measurement_service.calculate_signal_stats(signal_id, from_dt, to_dt)
        return stats
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error calculating stats: {str(e)}")

