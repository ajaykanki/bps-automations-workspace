from shared import get_env_file
from pydantic_settings import BaseSettings, SettingsConfigDict


class WorkerSettings(BaseSettings):
    model_config = SettingsConfigDict(
        env_file=get_env_file(),
        env_prefix="WORKER_",
        env_ignore_empty=True,
        extra="ignore",
    )

    concurrency: int = 1
    name: str | None = None
    queues: list[str] | None = None
    import_paths: list[str] = ["tasks"]
