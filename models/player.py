from dataclasses import dataclass
from models.spacecraft import SpacecraftState


@dataclass(slots=True)
class PlayerState:
    player_name: str
    credits: int
    spacecraft: SpacecraftState
    resources: dict[str, int]
