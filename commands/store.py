from utils.ui import fail
from systems.logistics.logistics import (
    move_resource_from_spacecraft_to_warehouse)
from config.resources import RESOURCES
from app.refresh import refresh_all


def handle_store(game, app, parts):
    if len(parts) < 3:
        return fail(
            game,
            app,
            message="USAGE: store iron 10"
        )

    move_resource_from_spacecraft_to_warehouse(game, app, parts, RESOURCES)

    refresh_all(app)
