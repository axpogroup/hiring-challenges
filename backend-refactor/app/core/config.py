"""Core configuration module."""
from functools import lru_cache
from app.core.settings import AppSettings

@lru_cache()
def get_settings() -> AppSettings:
    """Get cached application settings."""
    return AppSettings()

def load_config():
    """Deprecated: Use get_settings() instead."""
    return get_settings()

def get_config():
    """Another way to get config."""
    return AppSettings()
