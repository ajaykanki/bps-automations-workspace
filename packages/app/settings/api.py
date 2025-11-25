from shared import get_env_file
from pydantic_settings import BaseSettings, SettingsConfigDict


class APISettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=get_env_file(),
        env_prefix="API_",
        env_ignore_empty=True,
        extra="ignore",
    )

    host: str = "0.0.0.0"
    port: int = 8000
    key_header: str = "X-API-KEY"
    prefix: str = "/api"

    title: str = "Automation API"
    version: str = "0.1.0"
    description: str = "An API to interface with the automation stack"
