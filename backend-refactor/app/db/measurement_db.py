"""Database operations for measurements."""
from datetime import datetime
from typing import List, Dict, Optional
import random

def get_measurements(signal_ids: List[str], from_date: datetime, to_date: datetime) -> List[Dict]:
    """Get measurements for given signal IDs and date range."""
    measurements = []
    
    for signal_id in signal_ids:
        for i in range(5):
            #todo fake data, to be replaced with file access
            ts = from_date.timestamp() + (to_date.timestamp() - from_date.timestamp()) * i / 4
            measurements.append({
                "signal_id": signal_id,
                "timestamp": datetime.fromtimestamp(ts).isoformat(),
                "value": round(random.uniform(100, 500), 2),
                "unit": "kV"
            })

    return measurements

def fetch_measurements(signal_ids: List[str], start: datetime, end: datetime) -> List[Dict]:
    """Alternative function to fetch measurements."""
    return get_data(signal_ids, start, end)

def GetMeasurements(signalIds: List[str], fromDate: datetime, toDate: datetime) -> List[Dict]:
    return get_data(signalIds, fromDate, toDate)
