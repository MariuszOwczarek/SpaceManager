from utils.ui import fail, add_log
from systems.economy.economy import save_market_data


def move_ship(game, app, parts):
    destination = parts[1].capitalize()

    if destination not in game.planets:
        return fail(
            game,
            app,
            message="INVALID PLANET"
        )

    game.player.transit.destination = destination
    game.current_planet = (
        destination)
    save_market_data(game, destination)
    add_log(game, f"MOVED TO {destination.upper()}")

    app.load_layout()
    app.refresh_all()
