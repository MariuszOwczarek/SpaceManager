from systems.economy.turn import economy_system
from systems.population.turn import population_system
from systems.production.turn import production_system
from systems.contracts.turn import contract_system

TURN_SYSTEMS = [
    economy_system,
    population_system,
    production_system,
    contract_system
]


def run_turn_pipeline(game):
    for system in TURN_SYSTEMS:
        system(game)
