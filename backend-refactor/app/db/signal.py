"""Database operations for signals."""
import logging
from typing import List, Dict, Any

from app.core.config import get_settings
from app.utils.file_handlers import load_json_file

logger = logging.getLogger(__name__)

def load_signals() -> List[Dict[str, Any]]:
    """Load signals from JSON file."""
    settings = get_settings()
    logger.debug("Loading signals", extra={"path": settings.signals_path})

    data = load_json_file(settings.signals_path)
    logger.info("Signals loaded", extra={"count": len(data)})
    return data
