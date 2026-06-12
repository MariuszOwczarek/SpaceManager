from models.state.tasks.transport_task import TaskStatus
from utils.ui import fail
from config.balance.contracts import TASK_DECISION


def handle_task_decision(game, app, parts):
    try:
        number = int(parts[1])
    except ValueError:
        return fail(
            game,
            app,
            message="INVALID TASK NUMBER"
        )

    decision = parts[2].lower()

    if decision not in TASK_DECISION:
        return fail(
            game,
            app,
            message="WRONG DECISSION"
        )

    task = next(
        (
            task
            for task in game.tasks
            if task.task_id == number
        ),
        None
    )

    if task is None:
        return fail(
            game,
            app,
            message="TASK DOESNT EXIST"
        )

    if decision == TASK_DECISION[0]:
        task.status = TaskStatus.ACCEPTED

    elif decision == TASK_DECISION[1]:
        game.tasks.remove(task)
