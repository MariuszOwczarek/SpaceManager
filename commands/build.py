from config.facilities import FACILITIES
from utils.ui import fail
from systems.facilities import (get_building_credit_cost,
                                get_building_resource_cost)


def handle_build(game, app, parts):
    if len(parts) < 2:
        return fail(
            game,
            app,
            message="USAGE: build factory"
        )

    structure_key = parts[1].lower()

    if structure_key not in FACILITIES:
        return fail(
            game,
            app,
            message="INVALID BUILDING"
        )

    planet = game.planets[
        game.current_planet
    ]

    # =============================================
    # REQUIREMENTS
    # =============================================
    facility = (
        FACILITIES[
            structure_key
        ]
    )

    credit_cost = (
        get_building_credit_cost(structure_key, planet)
    )

    resource_costs = (
        get_building_resource_cost(structure_key, planet)
    )

    population_cost = (
        facility.population
    )

    # =============================================
    # CREDIT CHECK
    # =============================================
    if (
        game.player.credits
        < credit_cost
    ):
        return fail(
            game,
            app,
            message="NOT ENOUGH CREDITS"
        )

    # =============================================
    # POPULATION CHECK
    # =============================================
    if (
        planet.population < population_cost
    ):
        return fail(
            game,
            app,
            message="NOT ENOUGH POPULATION"
        )

    # =============================================
    # RESOURCE CHECK
    # =============================================
    for resource, amount in (
        resource_costs.items()
    ):
        if (
            game.player.resources[resource] < amount
        ):
            return fail(
                game,
                app,
                message=(
                    f"NOT ENOUGH "
                    f"{resource.upper()}"
                    )
            )

    # =============================================
    # PAY CREDITS
    # =============================================
    game.player.credits -= (
        credit_cost
    )

    # =============================================
    # PAY POPULATION
    # =============================================
    planet.population -= (
        population_cost
    )

    # =============================================
    # PAY RESOURCES
    # =============================================
    for resource, amount in (
        resource_costs.items()
    ):
        game.player.resources[resource] -= amount

    # =============================================
    # BUILD
    # =============================================
    planet.buildings[structure_key] += 1

    # =============================================
    # BUILDING EFFECTS
    # =============================================
    for attribute, value in (
        facility.effects.items()
    ):
        current = getattr(
            planet,
            attribute
        )

        setattr(
            planet,
            attribute,
            current + value
        )

    # =============================================
    # LOG
    # =============================================
    game.add_log(
        f"BUILT "
        f"{structure_key.upper()}"
    )
    app.refresh_all()
