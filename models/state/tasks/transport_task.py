from dataclasses import dataclass
from enum import Enum


class TaskStatus(Enum):
    AVAILABLE = "available"
    ACCEPTED = "accepted"
    PARTIALLY = "partially_delivered"
    COMPLETED = "completed"
    FAILED = "failed"


@dataclass(slots=True)
class TransportTask:
    task_id: int
    destination: str
    resource: str
    quantity: int
    turns_remaining: int
    reward: float
    status: TaskStatus
