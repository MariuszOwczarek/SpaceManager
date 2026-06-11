from systems.production.production import factory_production
from systems.population.population import hospital_population
from systems.economy.economy import (resource_price_change,
                                     resource_quantity_change)
from utils.ui import add_log
from config.resources import RESOURCES
from config.planets import PLANETS
from app.refresh import refresh_all


def handle_turn_end(game, app):
    game.turn += 1
    for planet_name, planet in game.planets.items():
        resource_price_change(planet, RESOURCES)
        resource_quantity_change(planet)
        factory_production(PLANETS, planet, planet_name, game)
        hospital_population(planet, planet_name, game)
    add_log(game, "TURN ENDED")
    refresh_all(app)
