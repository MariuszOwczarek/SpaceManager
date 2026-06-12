from models.state.tasks.transport_task import TaskStatus
from utils.ui import fail
from config.balance.contracts import TASK_DECISSION


def handle_task_decission(game, app, parts):
    try:
        number = int(parts[1])
    except ValueError:
        return fail(
            game,
            app,
            message="INVALID TASK NUMBER"
        )

    decission = parts[2].lower()

    if decission not in TASK_DECISSION:
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

    if decission == TASK_DECISSION[0]:
        task.status = TaskStatus.ACCEPTED

    elif decission == TASK_DECISSION[1]:
        game.tasks.remove(task)
