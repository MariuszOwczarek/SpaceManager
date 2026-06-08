from config.economy import RESOURCES, BASE_PRICES
from config.planets import PLANET_BONUSES
import random


def resource_price_change(planet):
    for resource in RESOURCES:
        stock = planet["resources"][resource]
        base_price = BASE_PRICES[resource]
        current_price = (
            planet["prices"][resource]
        )
        drift = random.randint(-5, 5)
        stock_pressure = 0

        if stock < 25:
            stock_pressure = random.randint(8, 20)
        elif stock > 150:
            stock_pressure = random.randint(-8, -2)

        new_price = current_price + drift + stock_pressure
        new_price += int(
            (base_price - new_price) * 0.15
        )

        minimum_price = int(
            base_price * 0.35
        )

        if new_price < minimum_price:
            new_price = minimum_price
        planet["prices"][resource] = (
            int(new_price)
            )


def resource_quantity_change(planet, planet_name):
    for resource in RESOURCES:
        resource_change = random.randint(-3, 8)
        new_resource = (planet["resources"][resource]
                        + resource_change)
        if new_resource < 0:
            new_resource = 0
        planet["resources"][resource] = new_resource

        cheap_resource = (
            PLANET_BONUSES[planet_name]["cheap"]
        )

        planet["prices"][cheap_resource] = int(
            planet["prices"][cheap_resource] * 0.9
        )
