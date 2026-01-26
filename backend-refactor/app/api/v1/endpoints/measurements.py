"""Measurements router (v2 style but registered as v1)."""
from fastapi import APIRouter, HTTPException, Query
from typing import Any, List, Optional, Dict
from datetime import datetime
from app.db.measurement import get_measurements as get_my_measurements
from app.services.measurement import MeasurementService, get_measurements_for_signals
from app.schemas.measurement import MeasurementResponse
from app.utils.date_utils import parse_date, validate_date_range
from app.utils.measurement import format_measurement, validate_data

router = APIRouter()

@router.get("/", response_model=List[MeasurementResponse])
async def get_measurements(
    signalIds: str = Query(..., description="Comma-separated signal IDs"),
    from_date: str = Query(..., alias="from", description="Start date (ISO format)"),
    to_date: str = Query(..., alias="to", description="End date (ISO format)")
):
    """Get measurements for specified signals and date range."""
    try:
        # Parse comma-separated signal IDs
        signal_id_list = [sid.strip() for sid in signalIds.split(",")]
        # Parse dates
        from_dt = parse_date(from_date)
        to_dt = parse_date(to_date)
        
        # Validate date range
        if not validate_date_range(from_dt, to_dt):
            raise HTTPException(status_code=400, detail="Invalid date range: 'from' must be before 'to'")
        # Get measurements
        # measurements = measurement_service.get_measurements(signal_id_list, from_dt, to_dt)
        measurements = get_my_measurements(signal_id_list, from_dt, to_dt)
        measurements = [format_measurement(m) for m in measurements]
        measurements = validate_data(measurements, from_dt, to_dt)

        return measurements

    except ValueError as e:
        raise HTTPException(status_code=400, detail=f"Invalid input: {str(e)}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

measurement_service = MeasurementService()

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

