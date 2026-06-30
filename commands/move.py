from utils.ui import fail
from systems.movement.movement import move_ship
from app.layout_manager import load_layout
from app.refresh import refresh_all


async def handle_move(game, app, parts):
    if len(parts) < 2:
        return fail(
            game,
            app,
            message="USAGE: move mars"
        )

    move_ship(game, app, parts)

    await load_layout(app)

    refresh_all(app)
