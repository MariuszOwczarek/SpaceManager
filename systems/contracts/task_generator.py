import random
from config.resources import RESOURCES
from config.planets import PLANETS
from models.state.tasks.transport_task import TransportTask, TaskStatus
from config.balance.contracts import (TASK_MIN_QUANTITY,
                                      TASK_MAX_QUANTITY,
                                      TASK_MIN_TURNS, TASK_MAX_TURNS,
                                      TASK_REWARD_MIN_MULTIPLIER,
                                      TASK_REWARD_MAX_MULTIPLIER)


def generate_transport_task(game):
    task_id = game.next_task_id
    game.next_task_id += 1
    destination = random.choice(list(PLANETS))
    resource = random.choice(list(RESOURCES))
    quantity = random.randint(TASK_MIN_QUANTITY, TASK_MAX_QUANTITY)
    turns_remaining = random.randint(TASK_MIN_TURNS, TASK_MAX_TURNS)
    reward = int(
        RESOURCES[resource].base_price
        * quantity
        * random.uniform(TASK_REWARD_MIN_MULTIPLIER,
                         TASK_REWARD_MAX_MULTIPLIER)
    )

    return TransportTask(
        task_id=task_id,
        destination=destination,
        resource=resource,
        quantity=quantity,
        turns_remaining=turns_remaining,
        reward=reward,
        status=TaskStatus.AVAILABLE
    )
