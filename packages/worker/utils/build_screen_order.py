from shared import log
from typing import Any
from tasks.sap.mappings import (
    ScreenOrder,
    Action,
)


def build_screen_order(screen_order: list[dict[str, Any]]) -> list[ScreenOrder]:
    log.info("Building screen order objects")
    return [
        ScreenOrder(
            name=screen.get("name"),
            post_actions=[Action(**action) for action in screen.get("post_actions")]
            if isinstance(screen.get("post_actions"), list)
            else Action(**screen.get("post_actions")),
        )
        if isinstance(screen, dict)
        else ScreenOrder(name=screen)
        for screen in screen_order
    ]
