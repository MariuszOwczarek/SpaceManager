from app.refresh import refresh_all
from commands.move import handle_move
from commands.buy import handle_buy
from commands.sell import handle_sell
from commands.build import handle_build
from commands.load import handle_load
from commands.store import handle_store
from commands.turn_end import handle_turn_end
from utils.ui import fail, add_log


# =====================================================
# COMMANDS
# =====================================================
async def process_command(app, command):
    parts = command.split()

    if not parts:
        return fail(
            game=app.game,
            app=app,
            message="PLEASE PROVDE COMMAND FROM A LIST"
        )

    action = parts[0].lower()

    if action in ["x", "exit"]:
        app.exit()
    elif action in ["m", "move"]:
        await handle_move(
            game=app.game,
            app=app,
            parts=parts
        )
    elif action in ["b", "buy"]:
        handle_buy(
            game=app.game,
            app=app,
            parts=parts
        )
    elif action in ["s", "sell"]:
        handle_sell(
            game=app.game,
            app=app,
            parts=parts
        )
    elif action == "build":
        handle_build(
            game=app.game,
            app=app,
            parts=parts
        )
    elif action in ["l", "load"]:
        handle_load(
            game=app.game,
            app=app,
            parts=parts
        )
    elif action in ["store"]:
        handle_store(
            game=app.game,
            app=app,
            parts=parts
        )
    elif action in ["e", "end"]:
        handle_turn_end(
            game=app.game,
            app=app
        )
    elif action == "help":
        add_log(app.game, "move mars | buy iron 10 | sell gold 5")
        refresh_all(app)
    else:
        add_log(app.game, "INVALID COMMAND")
        refresh_all(app)
