from typing import Optional

from pydantic_settings import BaseSettings
from functools import lru_cache


class MqttSettings(BaseSettings):
    class Config:
        env_file = '.env'
        env_prefix = 'mqtt_'

    host: str = "localhost"
    port: int = 1883
    username: Optional[str] = None
    password: Optional[str] = None


class Settings(BaseSettings):
    class Config:
        env_file = ".env"

    mqtt: MqttSettings = MqttSettings()
    logging_level: int = 30


@lru_cache()
def get_settings() -> Settings:
    return Settings()
