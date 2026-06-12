import random
from config.balance.economy import (
    ECONOMY_PRICE_DRIFT_MIN, ECONOMY_PRICE_DRIFT_MAX,
    ECONOMY_STOCK_PRESSURE_25_MIN,
    ECONOMY_STOCK_PRESSURE_25_MAX,
    ECONOMY_STOCK_PRESSURE_150_MIN,
    ECONOMY_STOCK_PRESSURE_150_MAX,
    ECONOMY_NEW_PRICE_MULTIPLIER,
    ECONOMY_MIN_PRICE_MULTIPLIER,
    ECONOMY_RESOURCE_CHANGE_MIN,
    ECONOMY_RESOURCE_CHANGE_MAX
)


def save_market_data(game, planet_name):
    market = game.planets[planet_name].market
    prices = {resource_key: market_item.price
              for resource_key, market_item in market.items()}
    game.market_memory[planet_name] = {
        "turn": game.turn,
        "prices": prices,
    }


def resource_price_change(planet, resources):
    for resource_key, market_item in planet.market.items():
        resource = resources[resource_key]
        market = planet.market[resource_key]
        stock = market.stock
        base_price = resource.base_price
        current_price = (
            market.price
        )
        drift = random.randint(ECONOMY_PRICE_DRIFT_MIN,
                               ECONOMY_PRICE_DRIFT_MAX)
        stock_pressure = 0

        if stock < 25:
            stock_pressure = random.randint(ECONOMY_STOCK_PRESSURE_25_MIN,
                                            ECONOMY_STOCK_PRESSURE_25_MAX)
        elif stock > 150:
            stock_pressure = random.randint(ECONOMY_STOCK_PRESSURE_150_MIN,
                                            ECONOMY_STOCK_PRESSURE_150_MAX)

        new_price = current_price + drift + stock_pressure
        new_price += int(
            (base_price - new_price) * ECONOMY_NEW_PRICE_MULTIPLIER
        )

        minimum_price = int(
            base_price * ECONOMY_MIN_PRICE_MULTIPLIER
        )

        if new_price < minimum_price:
            new_price = minimum_price
        market.price = (
            int(new_price)
            )


def resource_quantity_change(planet):
    for resource_key, resource in planet.market.items():
        market = planet.market[resource_key]
        resource_change = random.randint(ECONOMY_RESOURCE_CHANGE_MIN,
                                         ECONOMY_RESOURCE_CHANGE_MAX)
        market.stock += resource_change
        if market.stock < 0:
            market.stock = 0
