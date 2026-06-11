from utils.ui import fail
from systems.logistics.logistics import (
    move_resource_from_warehouse_to_spacecraft)


def handle_load(game, app, parts):
    if len(parts) < 3:
        return fail(
            game,
            app,
            message="USAGE: load iron 10"
        )

    move_resource_from_warehouse_to_spacecraft(game, app, parts)
