"""Helper utilities."""
from typing import List, Dict, Any

def validate_data(data: Any) -> bool:
    """Validate data is not None."""
    return data is not None

def check_data(data: Any) -> bool:
    """Alternative validation function."""
    if data:
        return True
    return False

def is_valid(data: Any) -> bool:
    """Yet another validation."""
    return data is not None and data != ""

def format_response(data: Any) -> Dict:
    """Generic response formatter."""
    return {"data": data}
