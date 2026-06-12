from systems.contracts.task_generator import generate_transport_task
from systems.production.production import factory_production
from systems.population.population import hospital_population
from systems.economy.economy import (resource_price_change,
                                     resource_quantity_change)
from utils.ui import add_log
from config.resources import RESOURCES
from config.planets import PLANETS
from app.refresh import refresh_all
import random


def handle_turn_end(game, app):
    game.turn += 1
    for planet_name, planet in game.planets.items():
        resource_price_change(planet, RESOURCES)
        resource_quantity_change(planet)
        factory_production(PLANETS, planet, planet_name, game)
        hospital_population(planet, planet_name, game)
    add_log(game, "TURN ENDED")

    # added task generator functionality for tests purpose only
    if random.random() <= 0.3:
        task = generate_transport_task(game)
        game.tasks.append(task)
        add_log(
            game,
            f"NEW TASK #{task.task_id}: "
            f"{task.destination.upper()} | "
            f"{task.resource.upper()} | "
            f"{task.quantity} | "
            f"{task.turns_remaining}T | "
            f"{task.reward}CR"
              )
    refresh_all(app)
