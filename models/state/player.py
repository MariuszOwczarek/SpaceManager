from dataclasses import dataclass
from models.definition.spacecraft import SpacecraftState
from models.state.transit import TransitState


@dataclass(slots=True)
class PlayerState:
    player_name: str
    credits: int
    spacecraft: SpacecraftState
    resources: dict[str, int]
    transit: TransitState | None = None
