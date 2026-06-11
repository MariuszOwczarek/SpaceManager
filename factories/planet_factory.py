from models.state.planet import PlanetState
from factories.market_factory import create_new_market
import random


def create_new_planet(definition, resources, facilities) -> PlanetState:
    return PlanetState(
            definition=definition,
            market=create_new_market(definition, resources),
            buildings={building: 0 for building in facilities},
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
