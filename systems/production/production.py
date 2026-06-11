from utils.ui import add_log


def factory_production(planets, planet, planet_name, game):
    factories = planet.buildings["factory"]
    if factories <= 0:
        return

    fuel_needed = factories * 2
    bonus_resource = planets[planet_name].resource_bonus

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

        add_log(
            game,
            f"{planet_name}: {bonus_resource.upper()} + {production}"
        )
