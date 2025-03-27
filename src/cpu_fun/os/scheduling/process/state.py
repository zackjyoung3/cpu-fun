from enum import StrEnum


class ProcessState(StrEnum):
    NEW = "new"
    READY = "ready"
    RUNNING = "running"
    WAITING = "waiting"  # aka BLOCKED
    TERMINATED = "terminated"
