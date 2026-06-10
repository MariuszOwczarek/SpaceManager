from utils.ui import fail


def move_ship(game, app, parts):
    destination = parts[1].capitalize()

    if destination not in game.planets:
        return fail(
            game,
            app,
            message="INVALID PLANET"
        )

    game.current_planet = (
        destination)

    game.save_market_data(destination)
    game.add_log(f"MOVED TO "
                 f"{destination.upper()}")

    app.load_layout()
    app.refresh_all()
