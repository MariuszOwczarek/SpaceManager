from dataclasses import dataclass


@dataclass(slots=True)
class Resource:
    name: str
    base_price: int
    weight: float
    category: str
