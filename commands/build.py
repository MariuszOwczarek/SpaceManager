from utils.ui import fail
from systems.facilities import build_facilities


def handle_build(game, app, parts):
    if len(parts) < 2:
        return fail(
            game,
            app,
            message="USAGE: build factory"
        )

    build_facilities(game, app, parts)
