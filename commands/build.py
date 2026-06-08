from config.buildings import BUILDINGS
from utils.ui import fail


def handle_build(game, app, parts):
    if len(parts) < 2:
        return fail(
            game,
            app,
            message="USAGE: build factory"
        )

    structure_key = parts[1].lower()

    if structure_key not in BUILDINGS:
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
    requirements = (
        BUILDINGS[
            structure_key
        ]
    )

    credit_cost = (
        requirements.credits
    )

    resource_costs = (
        requirements.resources
    )

    population_cost = (
        requirements.population
    )

    # =============================================
    # CREDIT CHECK
    # =============================================
    if (
        game.player["credits"]
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
        planet["population"] < population_cost
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
            game.player["resources"][resource] < amount
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
    game.player["credits"] -= (
        credit_cost
    )

    # =============================================
    # PAY POPULATION
    # =============================================
    planet["population"] -= (
        population_cost
    )

    # =============================================
    # PAY RESOURCES
    # =============================================
    for resource, amount in (
        resource_costs.items()
    ):
        game.player["resources"][
            resource
        ] -= amount

    # =============================================
    # BUILD
    # =============================================
    planet["buildings"][structure_key] += 1

    # =============================================
    # BUILDING EFFECTS
    # =============================================
    if structure_key == "hospital":
        planet["health"] += 10
        planet["happiness"] += 3
    elif structure_key == "school":
        planet["happiness"] += 12
    elif structure_key == "factory":
        planet["population"] += 5
        planet["happiness"] -= 2
    elif structure_key == "barracks":
        planet["safety"] += 15
        planet["happiness"] -= 5

    # =============================================
    # LOG
    # =============================================
    game.add_log(
        f"BUILT "
        f"{structure_key.upper()}"
    )
    app.refresh_all()
