from config.facilities import FACILITIES
from config.resources import RESOURCES
from config.planets import PLANETS
from config.spacecrafts import SPACECRAFTS
from factories.planet_factory import create_new_planet
from factories.player_factory import create_new_player


class GameState:
    def __init__(self):
        self.turn = 1
        self.current_planet = "Mars"
        self.logs = ["WELCOME COMMANDER"]
        self.market_memory = {}
        self.player = create_new_player(definition=SPACECRAFTS["shuttle"],
                                        resources=RESOURCES)
        self.planets = {
            name: create_new_planet(
                definition=definition,
                resources=RESOURCES,
                facilities=FACILITIES,
            )
            for name, definition in PLANETS.items()

        }
