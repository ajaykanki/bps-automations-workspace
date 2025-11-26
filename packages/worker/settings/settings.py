from shared import Settings
from .sap import SAPSettings
from .worker import WorkerSettings


class AppSettings(Settings):
    sap: SAPSettings = SAPSettings()
    worker: WorkerSettings = WorkerSettings()
    network_drives: dict[str, str] = {}


def _load_config() -> AppSettings:
    return AppSettings()


config = _load_config()
