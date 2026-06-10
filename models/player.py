from dataclasses import dataclass
from models.spacecraft import SpacecraftState
from config.resources import RESOURCES


@dataclass(slots=True)
class PlayerState:
    player_name: str
    credits: int
    spacecraft: SpacecraftState
    resources: dict[str, int]

    # =====================================================
    # CARGO
    # =====================================================
    def used_capacity(self):
        total = 0
        fuel_tank_capacity = (
            self.spacecraft.definition.fuel_tank_capacity
        )
        for resource_key, amount in self.resources.items():
            resource = RESOURCES[resource_key]
            if resource_key == "fuel":
                cargo_fuel = max(0, amount - fuel_tank_capacity)
                total += (cargo_fuel * resource.weight)
            else:
                total += (amount * resource.weight)
        return round(total, 1)

    def free_capacity(self):
        cargo_capacity = self.spacecraft.definition.cargo_capacity
        return round(cargo_capacity -
                     self.used_capacity(), 1)

    def fuel_used_capacity(self):
        fuel = self.resources["fuel"]
        return fuel

    def free_fuel(self):
        return round(self.spacecraft.definition.fuel_tank_capacity -
                     self.fuel_used_capacity(), 1)

    def cargo_fuel(self):
        total_fuel = self.resources["fuel"]
        fuel_capacity = self.spacecraft.definition.fuel_tank_capacity
        return max(0, total_fuel - fuel_capacity)
