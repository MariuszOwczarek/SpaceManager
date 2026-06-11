from factories.planet_generator import create_new_planet
from factories.player_generator import create_new_player


class GameState:
    def __init__(self):
        self.turn = 1
        self.current_planet = "Mars"
        self.logs = ["WELCOME COMMANDER"]
        self.market_memory = {}
        self.player = create_new_player()
        self.planets = {
            "Mars": create_new_planet("Mars"),
            "Venus": create_new_planet("Venus"),
            "Jupiter": create_new_planet("Jupiter"),
            "Saturn": create_new_planet("Saturn"),
            "Mercury": create_new_planet("Mercury"),
        }
