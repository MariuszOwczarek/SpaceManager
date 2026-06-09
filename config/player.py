from models.player import PlayerState
from models.spacecraft import SpacecraftState
from config.resources import RESOURCES
from config.spacecrafts import SPACECRAFTS

PLAYER_DATA = {
    "player": PlayerState(
        player_name="Mario",
        credits=50_000,
        spacecraft=SpacecraftState(
            definition=SPACECRAFTS["shuttle"],
            fuel=SPACECRAFTS["shuttle"].fuel_tank_capacity),
        resources={resource: 0 for resource in RESOURCES}
    )
}
