from systems.economy.trading import sell_resource
from utils.ui import fail
from config.resources import RESOURCES
from app.refresh import refresh_all


def handle_sell(game, app, parts):
    if len(parts) < 3:
        return fail(
            game,
            app,
            message="USAGE: sell gold 5"
        )

    sell_resource(game, app, parts, RESOURCES)

    refresh_all(app)
