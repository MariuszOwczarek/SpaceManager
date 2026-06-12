from config.resources import RESOURCES
from systems.economy.economy import (resource_price_change,
                                     resource_quantity_change)


def economy_system(game):
    for planet in game.planets.values():
        resource_price_change(planet,
                              RESOURCES)

        resource_quantity_change(planet)
