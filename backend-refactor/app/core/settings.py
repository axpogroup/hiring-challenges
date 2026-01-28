"""Application settings and environment variables."""
from pydantic_settings import BaseSettings, SettingsConfigDict

class AppSettings(BaseSettings):
    """Application settings loaded from environment."""
    app_name: str = "AssetAPI"
    api_version: str = "v1"
    debug_mode: bool = True
    log_level: str = "INFO"
    assets_path: str = "data/assets.json"
    signals_path: str = "data/signal.json"
    measurements_path: str = "data/measurements.csv"

    model_config = SettingsConfigDict(
        env_file=".env"
    )
