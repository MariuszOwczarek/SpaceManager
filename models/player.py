from dataclasses import dataclass


@dataclass(slots=True)
class Player:
    player_name: str
    credits: int
