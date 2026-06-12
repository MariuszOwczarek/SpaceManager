from models.state.transit import TransitState
from models.definition.spacecraft import SpacecraftState
from models.state.player import PlayerState
from config.balance.player import STARTING_CREDITS, PLAYER_NAME


def create_new_player(definition, resources) -> PlayerState:
    return PlayerState(
        player_name=PLAYER_NAME,
        credits=STARTING_CREDITS,
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
