from models.transit import TransitState
from models.spacecraft import SpacecraftState
from config.resources import RESOURCES
from config.spacecrafts import SPACECRAFTS
from models.player import PlayerState


def create_new_player() -> PlayerState:
    return PlayerState(
        player_name="Mario",
        credits=500_000,
        spacecraft=SpacecraftState(
            definition=SPACECRAFTS["shuttle"],
            fuel=SPACECRAFTS["shuttle"].fuel_tank_capacity),
        resources={resource: 0 for resource in RESOURCES},
        transit=TransitState(
            in_transit=False,
            turns_remaining=0,
            origin=None,
            destination=None
            )
        )
