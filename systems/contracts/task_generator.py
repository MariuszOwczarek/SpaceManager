import random
from config.resources import RESOURCES
from config.planets import PLANETS
from models.state.tasks.transport_task import TransportTask, TaskStatus


def generate_transport_task():

    destination = random.choice(list(PLANETS))
    resource = random.choice(list(RESOURCES))
    quantity = random.randint(10, 200)
    turns_remaining = random.randint(3, 6)
    reward = int(
        RESOURCES[resource].base_price
        * quantity
        * random.uniform(1.5, 2.5)
    )

    return TransportTask(
        destination=destination,
        resource=resource,
        quantity=quantity,
        turns_remaining=turns_remaining,
        reward=reward,
        status=TaskStatus.ACCEPTED
    )
