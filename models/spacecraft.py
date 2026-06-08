from dataclasses import dataclass


@dataclass(slots=True)
class SpacecraftDefinition:
    name: str
    type: str
    cargo_capacity: int
    fuel_tank_capacity: int
    fuel_usage: int
    speed: int
    scanner_range: int


@dataclass(slots=True)
class SpacecraftState:
    definition: SpacecraftDefinition
    fuel: int
