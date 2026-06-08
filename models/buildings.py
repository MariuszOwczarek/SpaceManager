from dataclasses import dataclass
from typing import Dict


@dataclass(slots=True)
class Buildings:
    name: str
    credits: int
    resources: Dict[str, int]
    population: int
