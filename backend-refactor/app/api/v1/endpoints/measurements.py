"""Measurements endpoints (v1)."""
from datetime import datetime
from typing import List
from fastapi import APIRouter, HTTPException, Query, Depends

from app.services.measurement import MeasurementService
from app.schemas.measurement import MeasurementResponse, MeasurementStatsResponse

router = APIRouter()

@router.get("", response_model=List[MeasurementResponse])
async def get_measurements(
    signal_ids: str = Query(..., description="Comma-separated signal IDs"),
    from_date: datetime = Query(
        ...,
        alias="from",
        description="Start datetime (ISO 8601)",
        openapi_examples={
            "default": {
                "summary": "Start of range",
                "value": "2024-01-01T00:00:00",
            }
        }
    ),
    to_date: datetime = Query(
        ...,
        alias="to",
        description="End datetime (ISO 8601)",
        openapi_examples={
            "default": {
                "summary": "End of range",
                "value": "2024-01-02T00:00:00",
            }
        }
    ),
    service: MeasurementService = Depends()
):
    """Get measurements for specified signals and date range."""
    if from_date >= to_date:
        raise HTTPException(
            status_code=400,
            detail="Invalid date range: 'from' must be before 'to'",
        )

    try:
        signal_id_list = [sid.strip() for sid in signal_ids.split(",")]

        return service.get_measurements(signal_id_list, from_date, to_date)

    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid date format: {str(e)}")

@router.get("/stats/{signal_id}", response_model=MeasurementStatsResponse)
async def get_signal_stats(
    signal_id: str,
    from_date: datetime = Query(
        ...,
        alias="from",
        description="Start datetime (ISO 8601)",
        openapi_examples={
            "default": {
                "summary": "Start of range",
                "value": "2024-01-01T00:00:00",
            }
        }
    ),
    to_date: datetime = Query(
        ...,
        alias="to",
        description="End datetime (ISO 8601)",
        openapi_examples={
            "default": {
                "summary": "End of range",
                "value": "2024-01-02T00:00:00",
            }
        }
    ),
    service: MeasurementService = Depends()
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
    if from_date >= to_date:
        raise HTTPException(
            status_code=400,
            detail="Invalid date range: 'from' must be before 'to'",
        )

    try:
        return service.calculate_signal_stats(signal_id, from_date, to_date)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
