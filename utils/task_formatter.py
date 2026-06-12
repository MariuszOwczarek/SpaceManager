def format_task(task):
    return (
        f"TASK #{task.task_id} | "
        f"{task.destination.upper()} | "
        f"{task.resource.upper()} | "
        f"{task.quantity} | "
        f"{task.turns_remaining}T | "
        f"{task.reward}CR | "
        f"{task.status.value.upper()}"
    )
