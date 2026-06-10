from config.player import PLAYER_DATA
from systems.world_generation import create_planet_state


class GameState:
    def __init__(self):
        self.turn = 1
        self.current_planet = "Mars"
        self.logs = ["WELCOME COMMANDER"]
        self.market_memory = {}
        self.player = PLAYER_DATA["player"]
        self.planets = {
            "Mars": create_planet_state("Mars"),
            "Venus": create_planet_state("Venus"),
            "Jupiter": create_planet_state("Jupiter"),
            "Saturn": create_planet_state("Saturn"),
            "Mercury": create_planet_state("Mercury"),
        }
