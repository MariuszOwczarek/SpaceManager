from config.resources import RESOURCES
from utils.ui import fail, add_log
from systems.capacity import free_capacity


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

    if free_capacity(game.player) < total_weight:
        return fail(
            game,
            app,
            message="NOT ENOUGH CARGO SPACE"
        )

    game.player.credits -= total_cost
    game.player.resources[resource_key] = (
        game.player.resources.get(resource_key, 0) + amount
    )
    market.stock -= amount
    
    add_log(game, f"BOUGHT " f"{amount} " f"{resource.name.upper()}")
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

    if game.player.resources.get(resource_key, 0) < amount:
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

    game.player.resources[resource_key] -= amount
    if game.player.resources[resource_key] <= 0:
        del game.player.resources[resource_key]
    game.player.credits += total
    market.stock += amount

    add_log(game, f"SOLD " f"{amount} " f"{resource.name.upper()}")
    app.refresh_all()
