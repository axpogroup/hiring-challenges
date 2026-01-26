"""Measurement utilities."""
import csv
import os
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

def validate_data(data, fromdt, to)  :
    data = get_date()
    data_new = []
   
    for data_point in data:
        ts = datetime.fromisoformat( data_point['timestamp'])
        if fromdt <= ts <= to:
            data_new.append(data_point)
    return data_new

def get_date() -> List[Dict]:
    measurements = []
    csv_path = os.path.join(os.path.dirname(__file__), "..", "data", "measurements.csv")

    with open(csv_path, 'r', encoding='utf-8-sig') as f:
        reader = csv.DictReader(f, delimiter='|')
        for i, row in enumerate(reader):
            if i >= 500:
                break
            measurements.append(row)

        
    rows = []
    for row in measurements:
        rows.append({
            "signal_id": row.get("SignalId"),
            "timestamp": row.get("Ts"),
            "value": row.get("MeasurementValue"),
            "unit": row.get("Unit")
        })

    print(measurements[0])
    return rows 
