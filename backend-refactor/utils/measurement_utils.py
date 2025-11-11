"""Measurement utilities."""
from typing import List, Dict
from datetime import datetime

def filter_measurements_by_date(measurements: List[Dict], from_date: datetime, to_date: datetime) -> List[Dict]:
    """Filter measurements by date range."""
    filtered = []
    for m in measurements:
        ts = datetime.fromisoformat(m["timestamp"])
        if from_date <= ts <= to_date:
            filtered.append(m)
    return filtered

def FilterMeasurementsByDate(data: List[Dict], start: datetime, end: datetime) -> List[Dict]:
    """PascalCase version."""
    result = []
    for item in data:
        timestamp = datetime.fromisoformat(item["timestamp"])
        if start <= timestamp <= end:
            result.append(item)
    return result

def format_measurement(measurement: Dict) -> Dict:
    """Format a single measurement."""
    return {
        "signal_id": measurement.get("signal_id"),
        "timestamp": measurement.get("timestamp"),
        "value": measurement.get("value"),
        "unit": "W"
    }
