import logging
from functools import lru_cache

from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AnyUrl

log = logging.getLogger("uvicorn")


class Settings(BaseSettings):
    database_hostname: str
    database_port: str
    database_password: str
    database_name: str
    database_username: str
    environment: str = "dev"
    testing: bool = bool(0)

    model_config = SettingsConfigDict(env_file=".env")


settings = Settings()


@lru_cache()
def get_settings() -> BaseSettings:
    log.info("Loading config settings from the environment...")
    return settings
