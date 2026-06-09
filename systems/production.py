from config.planets import PLANETS


def factory_production(planet, planet_name, game):
    factories = planet.buildings["factory"]
    if factories <= 0:
        return

    fuel_needed = factories * 2
    bonus_resource = PLANETS[planet_name].resource_bonus

    if "fuel" not in planet.market:
        return

    if bonus_resource not in planet.market:
        return

    fuel_market = planet.market["fuel"]
    bonus_market = planet.market[bonus_resource]

    if fuel_market.stock >= fuel_needed:
        fuel_market.stock -= fuel_needed
        production = factories * 15
        bonus_market.stock += production

        game.add_log(
            f"{planet_name}: "
            f"{bonus_resource.upper()} "
            f"+{production}"
        )

