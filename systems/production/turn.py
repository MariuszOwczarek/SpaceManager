from config.planets import PLANETS
from systems.production.production import factory_production


def production_system(game):
    for planet_name, planet in game.planets.items():
        factory_production(PLANETS, planet, planet_name, game)
