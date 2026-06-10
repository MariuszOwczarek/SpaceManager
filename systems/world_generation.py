from models.planet import PlanetState
from config.facilities import FACILITIES
from config.planets import PLANETS
from systems.economy import create_market
import random


def create_planet_state(name):
    return PlanetState(
            definition=PLANETS[name],
            market=create_market(name),
            buildings={building: 0 for building in FACILITIES},
            construction_modifier=random.randrange(5, 20, 5) / 10,
            population=random.randint(300, 1000),
            max_population=random.randrange(3000, 11_000, 1000),
            soldiers=0,
            health=random.randint(40, 80),
            happiness=random.randint(40, 80),
            safety=random.randint(50, 70),
            storage_capacity=0,
            storage={}
        )
