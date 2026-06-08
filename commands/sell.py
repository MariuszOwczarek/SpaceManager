from config.resources import RESOURCES
from utils.ui import fail


def handle_sell(game, app, parts):
    if len(parts) < 3:
        return fail(
            game,
            app,
            message="USAGE: sell gold 5"
        )

    resource_key = parts[1].lower()

    if resource_key not in RESOURCES:
        return fail(
            game,
            app,
            message="INVALID RESOURCE"
        )
    try:
        amount = int(parts[2])
    except ValueError:
        return fail(
            game,
            app,
            message="INVALID AMOUNT"
        )

    if amount <= 0:
        return fail(
            game,
            app,
            message="AMOUNT MUST BE > 0"
        )

    if game.player.resources[resource_key] < amount:
        return fail(
            game,
            app,
            message="NOT ENOUGH RESOURCES"
        )

    resource = RESOURCES[resource_key]
    planet = game.planets[game.current_planet]
    market = planet.market[resource_key]
    price = market.price
    total = amount * price

    # =============================================
    # TRANSACTION
    # =============================================
    game.player.resources[resource_key] -= amount
    game.player.credits += total
    market.stock += amount
    game.add_log(f"SOLD " f"{amount} " f"{resource.name.upper()}")
    app.refresh_all()
