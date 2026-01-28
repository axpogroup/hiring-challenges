"""Database operations for measurements."""
import logging
from datetime import datetime
from typing import List, Dict, Any

from app.core.config import get_settings
from app.utils.file_handlers import load_csv_file

logger = logging.getLogger(__name__)

def load_measurements_in_range(
    signal_ids: List[str],
    from_date: datetime,
    to_date: datetime
) -> List[Dict[str, Any]]:
    """Get measurements for given signal IDs and date range."""
    settings = get_settings()

    logger.debug(
        "Loading measurements from CSV",
        extra={"path": settings.measurements_path},
    )

    raw_measurements = load_csv_file(settings.measurements_path)
    
    # Use a set for faster lookup
    target_ids = set(signal_ids)
    
    # Define the exact format matching: 2021-11-07 23:51:40.298
    csv_ts_format = "%Y-%m-%d %H:%M:%S.%f"
    filtered_results = []
    skipped_rows = 0

    for row in raw_measurements:
        # Signal ID filter
        if row.get("SignalId") not in target_ids:
            continue
            
        try:
            # Parse the string to a comparable datetime object
            row_dt = datetime.strptime(row.get("Ts"), csv_ts_format)
            
            # Compare against your range
            if from_date <= row_dt <= to_date:
                filtered_results.append({
                    "signal_id": row.get("SignalId"),
                    "timestamp": row.get("Ts"),
                    # Convert decimal comma to float
                    "value": float(row.get("MeasurementValue").replace(',', '.'))
                })
        except (ValueError, TypeError, AttributeError):
            # Skip rows with missing or malformed data
            skipped_rows += 1
            continue

    logger.info(
        "Measurements filtered",
        extra={
            "requested_signals": len(target_ids),
            "results": len(filtered_results),
            "skipped_rows": skipped_rows,
        },
    )

    return filtered_results
