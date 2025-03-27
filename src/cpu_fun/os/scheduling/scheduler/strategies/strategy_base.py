"""
Prefer SchedulingStrategy as it confers same meaning as SchedulingPolicy would while signifying we are following
Strategy pattern
"""

from abc import ABC, abstractmethod

from cpu_fun.os.scheduling.process import Process
from cpu_fun.os.scheduling.events.action import Action


class SchedulingStrategyBase(ABC):
    @abstractmethod
    def handle_new_process(self, process: Process, time: int) -> Action | None:
        pass

    @abstractmethod
    def handle_process_req_io(self, process: Process, time: int) -> Action | None:
        pass

    @abstractmethod
    def handle_process_rec_io(self, process: Process, time: int) -> Action | None:
        pass

    @abstractmethod
    def get_next_process(self, time: int) -> Action | None:
        pass

    @abstractmethod
    def handle_process_complete(self, process: Process, time: int) -> Action | None:
        pass
