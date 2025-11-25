import os
import keyring
from shared.logger import log

ENV = os.getenv("ENV", "dev").lower()
PRODUCTION = ["prod", "production"]
DEVELOPMENT = ["dev", "development"]
KEYRING_SERVICE_NAME = os.getenv("KEYRING_SERVICE_NAME", "desktop-agent").lower()


def get_env_file():
    env_file = ".env" if ENV in PRODUCTION else f".env.{ENV}"
    return env_file


def get_keyring_password(
    key_name: str, service_name: str = KEYRING_SERVICE_NAME
) -> str | None:
    """
    Safely retrieve password from system keyring.

    Args:
        service_name: The name of the service to retrieve from keyring
        key_name: The key name to retrieve from keyring

    Returns:
        The password string if found, None otherwise
    """
    try:
        password = keyring.get_password(service_name, key_name)
        if password is None:
            log.debug("No keyring entry found for {}", key_name)

        return password
    except Exception as e:
        log.warning("Failed to retrieve {} from keyring: {}", key_name, e)
        return None
