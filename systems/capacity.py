from config.resources import RESOURCES


def used_capacity(player):
    total = 0
    fuel_tank_capacity = (
        player.spacecraft.definition.fuel_tank_capacity
    )
    for resource_key, amount in player.resources.items():
        resource = RESOURCES[resource_key]
        if resource_key == "fuel":
            cargo_fuel = max(0, amount - fuel_tank_capacity)
            total += (cargo_fuel * resource.weight)
        else:
            total += (amount * resource.weight)
    return round(total, 1)


def free_capacity(player):
    cargo_capacity = player.spacecraft.definition.cargo_capacity
    return round(cargo_capacity - used_capacity(player), 1)


def fuel_used_capacity(player):
    fuel = player.resources["fuel"]
    return fuel


def free_fuel(player):
    return round(player.spacecraft.definition.fuel_tank_capacity
                 - fuel_used_capacity(player), 1)


def cargo_fuel(player):
    total_fuel = player.resources["fuel"]
    fuel_capacity = player.spacecraft.definition.fuel_tank_capacity
    return max(0, total_fuel - fuel_capacity)
