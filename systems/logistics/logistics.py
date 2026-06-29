from utils.ui import add_log
from utils.ui import fail


def move_resource_from_warehouse_to_spacecraft(game, app, parts, resources):
    planet = game.planets[game.current_planet]
    planet_storage = planet.storage
    player_resources = game.player.resources
    spacecraft_free_capacity = game.player.free_capacity()
    resource_key = parts[1].lower()

    if resource_key not in resources:
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

    resource = resources[resource_key]
    total_weight = (
        amount * resource.weight
    )

    if spacecraft_free_capacity < total_weight:
        return fail(
            game,
            app,
            message="NOT ENOUGH FREE SPACE ON CARGO"
        )
    warehouse_amount = (
        planet_storage.get(resource_key, 0)
    )

    if warehouse_amount < amount:
        return fail(
            game,
            app,
            message="NOT ENOUGH QUANTITY"
                )
    else:
        planet_storage[resource_key] -= amount
        if planet_storage[resource_key] <= 0:
            del planet_storage[resource_key]

    player_resources[resource_key] = (
        player_resources.get(resource_key, 0)
        + amount)

    add_log(game, f"LOADED {amount} {resource_key.upper()}")


def move_resource_from_spacecraft_to_warehouse(game, app, parts, resources):
    planet = game.planets[game.current_planet]
    planet_free_storage = planet.free_storage()
    player_resources = game.player.resources
    resource_key = parts[1].lower()

    if resource_key not in resources:
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

    resource = resources[resource_key]
    total_weight = (
        amount * resource.weight
    )

    spacecraft_amount = player_resources.get(resource_key, 0)
    if spacecraft_amount < amount:
        return fail(
            game,
            app,
            message="NOT ENOUGH QUANTITY"
        )

    if total_weight > planet_free_storage:
        return fail(
            game,
            app,
            message="NOT ENOUGH FREE SPACE WAREHOUSE"
        )
    else:
        player_resources[resource_key] -= amount
        if player_resources[resource_key] <= 0:
            del player_resources[resource_key]

        planet.storage[resource_key] = (
            planet.storage.get(resource_key, 0)
            + amount
        )

    add_log(game, f"STORED {amount} {resource_key.upper()}")
