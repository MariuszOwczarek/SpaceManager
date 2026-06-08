from dataclasses import dataclass


@dataclass(slots=True)
class PlanetDefinition:
    name: str
    shortcut: str
    planet_type: str
    color: str
    cheap_resource: str
    resource_bonus: str
