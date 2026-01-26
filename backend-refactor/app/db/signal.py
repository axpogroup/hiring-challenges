"""Database operations for signals."""
from typing import List, Dict, Any
from app.core.config import get_settings
from app.utils.file_handlers import load_json_file

def load_signals() -> List[Dict[str, Any]]:
    """Load signals from JSON file."""
    settings = get_settings()
    return load_json_file(settings._path)
