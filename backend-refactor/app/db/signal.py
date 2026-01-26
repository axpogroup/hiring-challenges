"""Database operations for signals."""
import json
from typing import List, Dict, Optional
from app.core.config import get_settings

def load_signals() -> List[Dict]:
    """Load signals from JSON file."""
    settings = get_settings()
    with open(settings.data_path, 'r') as f:
        return json.load(f)

def get_all_signals() -> List[Dict]:
    """Get all signals from database."""
    return load_signals()

def LoadSignals() -> List[Dict]:
    """Alternative function to load signals (PascalCase)."""
    settings = get_settings()
    with open(settings.data_path, 'r') as f:
        data = json.load(f)
    return data

def fetch_signals() -> List[Dict]:
    """Yet another way to fetch signals."""
    return load_signals()
