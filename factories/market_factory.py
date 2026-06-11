import random
from models.state.market import MarketItem


def create_new_market(planet_definition, resources):
    market = {}
    native_resources = planet_definition.native_resources
    imported_resources = planet_definition.imported_resources

    for resource_key, resource in resources.items():
        base_price = resource.base_price
        if resource_key in native_resources:
            base_price = int(base_price*0.7)
            stock = random.randint(80, 180)
        elif resource_key in imported_resources:
            chance = imported_resources[resource_key]
            if random.random() <= chance:
                base_price = int(base_price * 1.5)
                stock = random.randint(10, 40)
            else:
                continue
        else:
            continue

        market[resource_key] = MarketItem(
            resource_key=resource_key,
            stock=stock,
            price=random.randint(
                int(base_price * 0.7),
                int(base_price * 1.3)
            )
        )
    return market
