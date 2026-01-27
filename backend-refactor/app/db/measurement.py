"""Database operations for measurements."""
from datetime import datetime
from typing import List, Dict, Any
from app.core.config import get_settings
from app.utils.file_handlers import load_csv_file

def load_measurements_in_range(
    signal_ids: List[str],
    from_date: datetime,
    to_date: datetime
) -> List[Dict[str, Any]]:
    """Get measurements for given signal IDs and date range."""
    settings = get_settings()
    raw_measurements = load_csv_file(settings.measurements_path)
    
    # Use a set for faster lookup
    target_ids = set(signal_ids)
    
    # Define the exact format matching: 2021-11-07 23:51:40.298
    csv_ts_format = "%Y-%m-%d %H:%M:%S.%f"

    filtered_results = []

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
            continue

    return filtered_results
