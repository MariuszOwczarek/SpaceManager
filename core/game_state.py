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
            "Mars": create_new_planet(definition=PLANETS["Mars"],
                                      resources=RESOURCES,
                                      facilities=FACILITIES),
            "Venus": create_new_planet(definition=PLANETS["Venus"],
                                       resources=RESOURCES,
                                       facilities=FACILITIES),
            "Jupiter": create_new_planet(definition=PLANETS["Jupiter"],
                                         resources=RESOURCES,
                                         facilities=FACILITIES),
            "Saturn": create_new_planet(definition=PLANETS["Saturn"],
                                        resources=RESOURCES,
                                        facilities=FACILITIES),
            "Mercury": create_new_planet(definition=PLANETS["Mercury"],
                                         resources=RESOURCES,
                                         facilities=FACILITIES),
        }
