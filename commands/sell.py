from systems.economy.trading import sell_resource
from utils.ui import fail


def handle_sell(game, app, parts):
    if len(parts) < 3:
        return fail(
            game,
            app,
            message="USAGE: sell gold 5"
        )

    sell_resource(game, app, parts)
