"""Database operations for assets."""
from typing import List, Dict, Any
from app.core.config import get_settings
from app.utils.file_handlers import load_json_file

def load_assets() -> List[Dict[str, Any]]:
    """Load assets from JSON file."""
    settings = get_settings()
    return load_json_file(settings.assets_path)
