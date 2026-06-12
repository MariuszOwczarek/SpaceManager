from models.state.planet import PlanetState
from factories.market_factory import create_new_market
import random
from config.balance.planet import (
    PLANET_CONSTRUCTION_MODIFIER_MIN,
    PLANET_CONSTRUCTION_MODIFIER_MAX,
    PLANET_CONSTRUCTION_MODIFIER_STEP,
    PLANET_POPULATION_MIN,
    PLANET_POPULATION_MAX,
    PLANET_MAX_POPULATION_MIN,
    PLANET_MAX_POPULATION_MAX,
    PLANET_MAX_POPULATION_STEP,
    PLANET_HEALTH_MIN, PLANET_HEALTH_MAX,
    PLANET_HAPPINESS_MIN, PLANET_HAPPINESS_MAX,
    PLANET_SAFETY_MIN, PLANET_SAFETY_MAX
)


def create_new_planet(definition, resources, facilities) -> PlanetState:
    return PlanetState(
            definition=definition,
            market=create_new_market(definition, resources),
            buildings={building: 0 for building in facilities},
            construction_modifier=(
                random.randrange(PLANET_CONSTRUCTION_MODIFIER_MIN,
                                 PLANET_CONSTRUCTION_MODIFIER_MAX,
                                 PLANET_CONSTRUCTION_MODIFIER_STEP) / 10),

            population=random.randint(PLANET_POPULATION_MIN,
                                      PLANET_POPULATION_MAX),

            max_population=random.randrange(PLANET_MAX_POPULATION_MIN,
                                            PLANET_MAX_POPULATION_MAX,
                                            PLANET_MAX_POPULATION_STEP),
            soldiers=0,

            health=random.randint(PLANET_HEALTH_MIN, PLANET_HEALTH_MAX),

            happiness=random.randint(PLANET_HAPPINESS_MIN,
                                     PLANET_HAPPINESS_MAX),

            safety=random.randint(PLANET_SAFETY_MIN, PLANET_SAFETY_MAX),

            storage_capacity=0,

            storage={}
        )
