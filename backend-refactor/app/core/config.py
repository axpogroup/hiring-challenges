"""Core configuration module."""
from functools import lru_cache
from app.core.settings import AppSettings

@lru_cache()
def get_settings() -> AppSettings:
    """Get cached application settings."""
    return AppSettings()
