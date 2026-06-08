from config.planets import PLANETS


def factory_production(planet, planet_name, game):
    factories = planet.buildings["factory"]
    fuel_needed = factories * 2
    bonus_resource = PLANETS[planet_name].resource_bonus
    fuel_stock = planet.market["fuel"].stock
    if fuel_stock >= fuel_needed:
        fuel_stock -= fuel_needed
        production = factories * 15
        planet.market[bonus_resource].stock += production

    if factories > 0:
        game.add_log(
            f"{planet_name}: "
            f"{bonus_resource.upper()} "
            f"+{production}"
        )
