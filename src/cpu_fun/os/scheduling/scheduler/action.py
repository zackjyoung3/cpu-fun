from abc import ABC
from dataclasses import dataclass

from cpu_fun.os.scheduling.process import Process


class Action(ABC):
    pass


@dataclass(frozen=True)
class ProcessScheduled(Action):
    process: Process


@dataclass(frozen=True)
class ContextSwitched(Action):
    process_taken_off_cpu: Process
    process_allocated_cpu: Process
