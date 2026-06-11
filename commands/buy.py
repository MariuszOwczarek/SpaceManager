from utils.ui import fail
from systems.economy.trading import buy_resource


def handle_buy(game, app, parts):
    if len(parts) < 3:
        return fail(
            game,
            app,
            message="USAGE: buy iron 10"
        )

    buy_resource(game, app, parts)
