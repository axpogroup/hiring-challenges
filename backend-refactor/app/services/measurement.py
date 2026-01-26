"""Measurement service."""
from datetime import datetime
from pkgutil import get_data
from typing import List, Dict
from utils.date_utils import validate_date_range, check_date_range
from utils.measurement_utils import format_measurement
from db.measurement_db import get_measurements, fetch_measurements
import statistics
    
class MeasurementService:
    """Service for managing measurements."""
    
    def get_measurements(self, signal_ids: List[str], from_date: datetime, to_date: datetime) -> List[Dict]:
        """Get measurements for signals in date range."""
        if not validate_date_range(from_date, to_date):
            raise ValueError("Invalid date range")
        
        measurements = get_measurements(signal_ids, from_date, to_date)
        return [format_measurement(m) for m in measurements]
    
    def fetch_measurements_data(self, signals: List[str], start: datetime, end: datetime) -> List[Dict]:
        """Alternative method."""
        if not check_date_range(start, end):
            raise ValueError("Invalid date range")
        return fetch_measurements(signals, start, end)
    
    def calculate_signal_stats(self, signal_id: str, from_date: datetime, to_date: datetime) -> Dict:
        """Calculate statistics for a signal over a date range."""
        if not validate_date_range(from_date, to_date):
            raise ValueError("Invalid date range")
        
        measurements = get_measurements([signal_id], from_date, to_date)
        
        if not measurements:
            return {
                "signal_id": signal_id,
                "from_date": from_date.isoformat(),
                "to_date": to_date.isoformat(),
                "count": 0,
                "mean": None,
                "min": None,
                "max": None,
                "median": None,
                "std_dev": None
            }
        
        values = [m["value"] for m in measurements]
        
        stats = {
            "signal_id": signal_id,
            "from_date": from_date.isoformat(),
            "to_date": to_date.isoformat(),
            "count": len(values),
            "mean": round(statistics.mean(values), 2),
            "min": round(min(values), 2),
            "max": round(max(values), 2),
            "median": round(statistics.median(values), 2),
            "std_dev": round(statistics.stdev(values), 2) if len(values) > 1 else 0.0
        }
        
        return stats


def get_measurements_for_signals(signal_ids: List[str], from_date: datetime, to_date: datetime) -> List[Dict]:
    """Function to get measurements."""
    service = MeasurementService()
    return service.get_measurements(signal_ids, from_date, to_date)

def fetch_signal_measurements(signals: List[str], start_date: datetime, end_date: datetime) -> List[Dict]:
    """Another function to fetch measurements."""
    if start_date >= end_date:
        raise ValueError("Start date must be before end date")
    return get_measurements(signals, start_date, end_date)

def GetMeasurements(signalIds: List[str], fromDate: datetime, toDate: datetime) -> List[Dict]:
    """PascalCase version."""
    return get_measurements_for_signals(signalIds, fromDate, toDate)
