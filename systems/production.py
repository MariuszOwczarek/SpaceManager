from config.planets import PLANET_BONUSES


def factory_production(planet, planet_name, game):
    factories = planet["buildings"]["factory"]
    fuel_needed = factories * 2
    bonus_resource = PLANET_BONUSES[planet_name]["resource_bonus"]
    if planet["resources"]["fuel"] >= fuel_needed:
        planet["resources"]["fuel"] -= fuel_needed
        production = factories * 15
        planet["resources"][bonus_resource] += production

    if factories > 0:
        game.add_log(
            f"{planet_name}: "
            f"{bonus_resource.upper()} "
            f"+{production}"
        )
