from dataclasses import dataclass
from typing import Dict


@dataclass(slots=True)
class Facility:
    name: str
    credits: int
    resources: Dict[str, int]
    population: int
    effects: dict[str, int]
