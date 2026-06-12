import random
from models.state.market import MarketItem
from config.balance.market import (
    NATIVE_RESOURCES_BASE_PRICE_MULTIPLIER,
    NATIVE_RESOURCES_STOCK_MAX_QUANTITY,
    NATIVE_RESOURCES_STOCK_MIN_QUANTITY,
    IMPORTED_RESOURCES_BASE_PRICE_MULTIPLIER,
    IMPORTED_RESOURCES_STOCK_MAX_QUANTITY,
    IMPORTED_RESOURCES_STOCK_MIN_QUANTITY,
    STANDARD_RESOURCES_MIN_BASE_PRICE_MULTIPLIER,
    STANDARD_RESOURCES_MAX_BASE_PRICE_MULTIPLIER
)


def create_new_market(planet_definition, resources):
    market = {}
    native_resources = planet_definition.native_resources
    imported_resources = planet_definition.imported_resources

    for resource_key, resource in resources.items():
        base_price = resource.base_price
        if resource_key in native_resources:
            base_price = int(base_price
                             * NATIVE_RESOURCES_BASE_PRICE_MULTIPLIER)
            stock = random.randint(NATIVE_RESOURCES_STOCK_MIN_QUANTITY,
                                   NATIVE_RESOURCES_STOCK_MAX_QUANTITY)
        elif resource_key in imported_resources:
            chance = imported_resources[resource_key]
            if random.random() <= chance:
                base_price = int(base_price
                                 * IMPORTED_RESOURCES_BASE_PRICE_MULTIPLIER)
                stock = random.randint(IMPORTED_RESOURCES_STOCK_MIN_QUANTITY,
                                       IMPORTED_RESOURCES_STOCK_MAX_QUANTITY)
            else:
                continue
        else:
            continue

        market[resource_key] = MarketItem(
            resource_key=resource_key,
            stock=stock,
            price=random.randint(
                int(base_price * STANDARD_RESOURCES_MIN_BASE_PRICE_MULTIPLIER),
                int(base_price * STANDARD_RESOURCES_MAX_BASE_PRICE_MULTIPLIER)
            )
        )
    return market
