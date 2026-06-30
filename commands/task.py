from utils.ui import fail
from systems.contracts.task_choose import handle_task_decision
from app.refresh import refresh_all


def handle_task(game, app, parts):
    if len(parts) < 3:
        return fail(
            game,
            app,
            message="USAGE: task 1 accept / task 1 reject"
        )

    handle_task_decision(game, app, parts)

    refresh_all(app)
