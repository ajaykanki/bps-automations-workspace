from settings import config
from pathlib import Path


def map_container_path_to_network(container_path: str, network_drive: str) -> Path:
    """
    Convert a container path to a network UNC path by mapping it to a configured network drive.

    This function takes a container path (starting with '/') and maps it to a UNC path
    using the network drive configuration specified in the application settings.
    It handles cases where the container path may already contain the network drive root.

    Args:
        container_path (str): The container path to convert (e.g., '/so_automation/artifacts/po_working.xlsx')
        network_drive (str): The key for the network drive configuration in settings

    Returns:
        Path: A Path object representing the mapped UNC path (e.g., '\\\\ip_address\\SSC-Merc_SO_Team\\so_automation\\artifacts\\po_working.xlsx')

    Raises:
        ValueError: If the specified network drive is not found in the configuration

    Example:
        >>> # Assuming config.network_drives['so_team'] = '//192.168.1.100/SSC-Merc_SO_Team'
        >>> result = map_container_path_to_network('/so_automation/artifacts/report.xlsx', 'so_team')
        >>> print(result)
        Path('//192.168.1.100/SSC-Merc_SO_Team/so_automation/artifacts/report.xlsx')
    """

    base_unc = config.network_drives.get(network_drive)
    if not base_unc:
        raise ValueError(f"Network drive {network_drive} not found in config")

    container_path = Path(container_path).as_posix()
    base_unc_path = Path(base_unc)
    base_root = base_unc_path.name

    if base_root in container_path:
        rel = container_path.split(base_root, 1)[1].lstrip("/")
    else:
        rel = container_path.lstrip("/")

    final = base_unc_path / Path(rel)
    return final
