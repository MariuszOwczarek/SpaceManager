from dataclasses import dataclass
from models.state.market import MarketItem
from models.definition.planet import PlanetDefinition


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
