from config.resources import RESOURCES
from utils.ui import fail


def buy_resource(game, app, parts):
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

    resource = RESOURCES[resource_key]
    planet = game.planets[game.current_planet]

    if resource_key not in planet.market:
        return fail(
            game,
            app,
            message="INVALID RESOURCE"
        )
    market = planet.market[resource_key]
    available = market.stock
    price = market.price
    total_cost = amount * price
    total_weight = amount * resource.weight

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

    if game.player.credits < total_cost:
        return fail(
            game,
            app,
            message="NOT ENOUGH CREDITS"
        )

    if game.player.free_capacity() < total_weight:
        return fail(
            game,
            app,
            message="NOT ENOUGH CARGO SPACE"
        )

    # =============================================
    # TRANSACTION
    # =============================================
    game.player.credits -= total_cost
    game.player.resources[resource_key] += amount
    market.stock -= amount
    game.add_log(f"BOUGHT " f"{amount} " f"{resource.name.upper()}")
    app.refresh_all()


def sell_resource(game, app, parts):
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
