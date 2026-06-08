from config.economy import RESOURCES, RESOURCE_WEIGHT
from utils.ui import fail


def handle_buy(game, app, parts):
    if len(parts) < 3:
        return fail(
            game,
            app,
            message="USAGE: buy iron 10"
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

    planet = game.planets[game.current_planet]
    available = planet["resources"][resource]
    price = planet["prices"][resource]
    total_cost = amount * price
    total_weight = amount * RESOURCE_WEIGHT[resource]

    # =============================================
    # VALIDATION
    # =============================================
    if amount <= 0:
        return fail(
            game,
            app,
            message="AMOUNT MUST BE > 0"
        )

    if available < amount:
        return fail(
            game,
            app,
            message="NOT ENOUGH PLANET STOCK"
        )

    if game.player["credits"] < total_cost:
        return fail(
            game,
            app,
            message="NOT ENOUGH CREDITS"
        )

    if game.free_capacity() < total_weight:
        return fail(
            game,
            app,
            message="NOT ENOUGH CARGO SPACE"
        )

    # =============================================
    # TRANSACTION
    # =============================================
    game.player["credits"] -= total_cost
    game.player["resources"][resource] += amount
    planet["resources"][resource] -= amount
    game.add_log(f"BOUGHT " f"{amount} " f"{resource.upper()}")
    app.refresh_all()
