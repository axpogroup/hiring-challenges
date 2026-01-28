"""Database operations for assets."""
import logging
from typing import List, Dict, Any

from app.core.config import get_settings
from app.utils.file_handlers import load_json_file

logger = logging.getLogger(__name__)

def load_assets() -> List[Dict[str, Any]]:
    """Load assets from JSON file."""
    settings = get_settings()
    logger.debug("Loading assets", extra={"path": settings.assets_path})

    data = load_json_file(settings.assets_path)
    logger.info("Assets loaded", extra={"count": len(data)})

    return data