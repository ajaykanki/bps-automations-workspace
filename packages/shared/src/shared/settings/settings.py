from shared.logger import log
from shared.utils import ENV, DEVELOPMENT, KEYRING_SERVICE_NAME, get_env_file
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import PostgresDsn


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=get_env_file(), extra="ignore")
    env: str = ENV
    keyring_service_name: str = KEYRING_SERVICE_NAME
    database_url: PostgresDsn | None = None

    @property
    def is_dev(self) -> bool:
        return self.env in DEVELOPMENT

    def model_post_init(self, context):
        if self.database_url is None:
            log.warning("DATABASE_URL is not set in environment variables")

        return super().model_post_init(context)
