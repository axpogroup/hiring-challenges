"""Application settings and environment variables."""
import os
from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    """Application settings loaded from environment."""
    app_name: str = "AssetAPI"
    api_version: str = "v1"
    debug_mode: bool = True
    data_path: str = "data/signal.json"
    
    class Config:
        env_file = ".env"

class Settings(BaseSettings):
    """Alternative settings class."""
    APP_NAME: str = "AssetAPI"
    API_VERSION: str = "v1"
    
    class Config:
        env_file = ".env"
