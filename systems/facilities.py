from models.state.planet import PlanetState
from utils.ui import fail, add_log
from app.refresh import refresh_all


def get_building_credit_cost(facilities, facility_key: str,
                             planet: PlanetState):
    facility = facilities[facility_key]
    return int(facility.credits * planet.construction_modifier)


def get_building_resource_cost(facilities, facility_key: str,
                               planet: PlanetState):
    facility = facilities[facility_key]
    return {resource: int((amount * planet.construction_modifier))
            for resource, amount in (
                facility.resources.items()
                                     )
            }


def build_facilities(game, app, parts, facilities):
    structure_key = parts[1].lower()

    if structure_key not in facilities:
        return fail(
            game,
            app,
            message="INVALID BUILDING"
        )

    planet = game.planets[
        game.current_planet
    ]

    facility = (
        facilities[
            structure_key
        ]
    )

    credit_cost = (
        get_building_credit_cost(facilities, structure_key, planet)
    )

    resource_costs = (
        get_building_resource_cost(facilities, structure_key, planet)
    )

    population_cost = (
        facility.population
    )

    if (
        game.player.credits
        < credit_cost
    ):
        return fail(
            game,
            app,
            message="NOT ENOUGH CREDITS"
        )

    if (
        planet.population < population_cost
    ):
        return fail(
            game,
            app,
            message="NOT ENOUGH POPULATION"
        )

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

    game.player.credits -= (
        credit_cost
    )

    planet.population -= (
        population_cost
    )

    for resource, amount in (
        resource_costs.items()
    ):
        game.player.resources[resource] -= amount

    planet.buildings[structure_key] += 1

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

    add_log(game, f"BUILT {structure_key.upper()}")
    refresh_all(app)
