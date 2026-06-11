
from dataclasses import dataclass


@dataclass
class TransitState:
    in_transit: bool
    turns_remaining: int
    origin: str | None = None
    destination: str | None = None
