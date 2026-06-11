from dataclasses import dataclass


@dataclass(slots=True)
class ResourceDefinition:
    name: str
    base_price: int
    weight: float
    category: str
