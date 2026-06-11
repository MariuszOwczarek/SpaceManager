from utils.ui import fail
from systems.movement.movement import move_ship


def handle_move(game, app, parts):
    if len(parts) < 2:
        return fail(
            game,
            app,
            message="USAGE: move mars"
        )

    move_ship(game, app, parts)
