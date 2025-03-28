from cpu_fun.os.scheduling.events.action import Action
from cpu_fun.os.scheduling.events.event import Event, EventType
from cpu_fun.os.scheduling.process import Process
from cpu_fun.os.scheduling.scheduler.strategies import SchedulingStrategyBase


class Scheduler:
    _current_proc_allocated_cpu: Process | None

    def __init__(self, scheduling_strat: SchedulingStrategyBase, global_clock_time: int = 0) -> None:
        self._scheduling_strat = scheduling_strat
        self._clock = global_clock_time
        self._current_proc_allocated_cpu = None

    def tick(self, time_unit: int) -> None:
        self._clock += time_unit

    def handle(self, event: Event) -> Action | None:
        match event.type:
            case EventType.PROC_ARRIVED:
                return self._scheduling_strat.handle_new_process(event.associated_process, self._clock)
            case EventType.PROC_REC_IO:
                return self._scheduling_strat.handle_process_req_io(event.associated_process, self._clock)
            case EventType.PROC_REQ_IO:
                return self._scheduling_strat.handle_process_rec_io(event.associated_process, self._clock)
            case EventType.PROC_COMPLETE:
                return self._scheduling_strat.handle_process_complete(event.associated_process, self._clock)
            case _:
                raise ValueError(f"Unknown event type {event.type}")
