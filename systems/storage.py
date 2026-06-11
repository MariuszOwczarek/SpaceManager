from config.resources import RESOURCES


def used_storage(planet):
    total = 0.0
    for resource_key, amount in planet.storage.items():
        resource = RESOURCES[resource_key]
        total += (amount * resource.weight)
    return round(total, 1)


def free_storage(planet):
    return round(
        planet.storage_capacity - used_storage(planet),
        1
    )
