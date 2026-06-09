from dataclasses import dataclass
from models.market import MarketItem
from config.resources import RESOURCES


@dataclass(slots=True)
class PlanetDefinition:
    name: str
    shortcut: str
    planet_type: str
    color: str
    cheap_resource: str
    resource_bonus: str
    native_resources: list[str]
    imported_resources: dict[str, float]
    routes: dict[str, int]
    is_homeworld: bool


@dataclass(slots=True)
class PlanetState:
    definition: PlanetDefinition
    market: dict[str, MarketItem]
    buildings: dict[str, int]
    construction_modifier: float
    population: int
    max_population: int
    soldiers: int
    health: int
    happiness: int
    safety: int
    storage_capacity: int
    storage: dict[str, int]

    def used_storage(self):
        total = 0.0
        for resource_key, amount in self.storage.items():
            resource = RESOURCES[resource_key]
            total += (amount * resource.weight)
        return round(total, 1)

    def free_storage(self):
        return round(
            self.storage_capacity - self.used_storage(),
            1
        )
