from utils.ui import fail
from systems.facilities import build_facilities
from config.facilities import FACILITIES
from app.refresh import refresh_all


def handle_build(game, app, parts):
    if len(parts) < 2:
        return fail(
            game,
            app,
            message="USAGE: build factory"
        )

    build_facilities(game, app, parts, FACILITIES)

    refresh_all(app)
