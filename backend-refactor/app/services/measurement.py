"""Measurement service."""
import statistics
from datetime import datetime
from typing import List, Dict
from app.db.signal import load_signals
from app.db.measurement import load_measurements_in_range
from app.utils.date_utils import validate_date_range
    
class MeasurementService:
    """Service for managing measurements."""
    
    def get_measurements(self, signal_ids: List[str], from_date: datetime, to_date: datetime) -> List[Dict]:
        """Get measurements for signals in date range."""
        if not validate_date_range(from_date, to_date):
            raise ValueError("Invalid date range: 'from' must be before 'to'")
        
        measurements = load_measurements_in_range(signal_ids, from_date, to_date)
        # Load signals to get units from signals
        signals = load_signals()

        # Create a lookup for Units (SignalId -> Unit)        
        unit_map = {s.get("SignalId"): s.get("Unit") for s in signals}

        for m in measurements:
            sig_id = m.get("signal_id")
            m['unit'] = unit_map.get(sig_id, "N/A")
            
        return measurements

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
