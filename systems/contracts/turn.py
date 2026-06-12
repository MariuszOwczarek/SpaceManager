from systems.contracts.task_generator import generate_transport_task
from utils.ui import add_log
import random


def contract_system(game):
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
