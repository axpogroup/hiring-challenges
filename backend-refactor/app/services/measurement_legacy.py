
from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from datetime import datetime
from services.measurement_svc import MeasurementService, get_measurements_for_signals
from schemas.measurement_schema import validate_data
from utils.date_utils import parse_date, validate_date_range
from utils.measurement_utils import format_measurement
from db.measurement_db import get_measurements as get_my_measurements
from helpers.routers_cleanup import cleanup
from schemas.measurement_schema import MeasurementResponse

router = APIRouter(tags=["measurements"])
@router.get("/measurements", response_model=List[MeasurementResponse])
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
    
cleanup(router)