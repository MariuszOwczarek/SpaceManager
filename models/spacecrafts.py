from dataclasses import dataclass


@dataclass(slots=True)
class Spacecrafts:
    name: str
    type: str
    cargo_capacity: int
    fuel_tank: int
    fuel_usage: int
    speed: int
    scanner_range: int
