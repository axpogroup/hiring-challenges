"""Alternative database module."""
import json
from typing import List, Dict
from core.settings import AppSettings

def read_signal_data() -> List[Dict]:
    """Read signal data from file."""
    settings = AppSettings()
    with open(settings.data_path, 'r') as file:
        return json.load(file)

def query_signals() -> List[Dict]:
    """Query all signals."""
    return read_signal_data()
