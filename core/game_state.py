from systems.world_generation import create_planet_state
from config.player import create_new_player


class GameState:
    def __init__(self):
        self.turn = 1
        self.current_planet = "Mars"
        self.logs = ["WELCOME COMMANDER"]
        self.market_memory = {}
        self.player = create_new_player()
        self.planets = {
            "Mars": create_planet_state("Mars"),
            "Venus": create_planet_state("Venus"),
            "Jupiter": create_planet_state("Jupiter"),
            "Saturn": create_planet_state("Saturn"),
            "Mercury": create_planet_state("Mercury"),
        }
