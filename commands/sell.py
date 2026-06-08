from config.economy import RESOURCES
from utils.ui import fail


def handle_sell(game, app, parts):
    if len(parts) < 3:
        return fail(
            game,
            app,
            message="USAGE: sell gold 5"
        )

    resource = parts[1].lower()

    if resource not in RESOURCES:
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

    if game.player["resources"][resource] < amount:
        return fail(
            game,
            app,
            message="NOT ENOUGH RESOURCES"
        )

    planet = game.planets[game.current_planet]
    price = planet["prices"][resource]
    total = amount * price

    # =============================================
    # TRANSACTION
    # =============================================
    game.player["resources"][resource] -= amount
    game.player["credits"] += total
    planet["resources"][resource] += amount
    game.add_log(f"SOLD " f"{amount} " f"{resource.upper()}")
    app.refresh_all()
