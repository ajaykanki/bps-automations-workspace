from shared import Settings
from .api import APISettings
from .o365 import O365Settings
from .wmill import WmillSettings


class AppSettings(Settings):
    api: APISettings = APISettings()
    o365: O365Settings = O365Settings()
    wmill: WmillSettings = WmillSettings()


def _load_config() -> AppSettings:
    return AppSettings()


config = _load_config()
