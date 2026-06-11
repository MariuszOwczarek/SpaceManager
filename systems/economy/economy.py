from config.resources import RESOURCES
import random


def save_market_data(game, planet_name):
    market = game.planets[planet_name].market
    prices = {resource_key: market_item.price
              for resource_key, market_item in market.items()}
    game.market_memory[planet_name] = {
        "turn": game.turn,
        "prices": prices,
    }


def resource_price_change(planet):
    for resource_key, market_item in planet.market.items():
        resource = RESOURCES[resource_key]
        market = planet.market[resource_key]
        stock = market.stock
        base_price = resource.base_price
        current_price = (
            market.price
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
        market.price = (
            int(new_price)
            )


def resource_quantity_change(planet):
    for resource_key, resource in planet.market.items():
        market = planet.market[resource_key]
        resource_change = random.randint(-3, 8)
        market.stock += resource_change
        if market.stock < 0:
            market.stock = 0
