from dataclasses import dataclass
from models.market import MarketItem


@dataclass(slots=True)
class PlanetDefinition:
    name: str
    shortcut: str
    planet_type: str
    color: str
    cheap_resource: str
    resource_bonus: str


@dataclass(slots=True)
class PlanetState:
    definition: PlanetDefinition
    market: dict[str, MarketItem]
    buildings: dict[str, int]
    construction_modifier: float
    population: int
    max_population: int
    health: int
    happiness: int
    safety: int
