from models.state.transit import TransitState
from models.definition.spacecraft import SpacecraftState
from models.state.player import PlayerState


def create_new_player(definition, resources) -> PlayerState:
    return PlayerState(
        player_name="Mario",
        credits=500_000,
        spacecraft=SpacecraftState(
            definition=definition,
            fuel=definition.fuel_tank_capacity),
        resources={},
        transit=TransitState(
            in_transit=False,
            turns_remaining=0,
            origin=None,
            destination=None
            )
        )
