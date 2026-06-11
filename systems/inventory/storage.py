def used_storage(planet, resources):
    total = 0.0
    for resource_key, amount in planet.storage.items():
        resource = resources[resource_key]
        total += (amount * resource.weight)
    return round(total, 1)


def free_storage(planet, resources):
    return round(
        planet.storage_capacity - used_storage(planet, resources),
        1
    )
