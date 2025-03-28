from abc import ABC
from collections import deque
from dataclasses import dataclass
from enum import StrEnum


class PhaseType(StrEnum):
    BURST = "Burst"
    IO = "IO"
    TERMINATED = "Terminated"


@dataclass
class JobPhase:
    type: PhaseType
    duration: int


@dataclass
class SimJob(ABC):
    id: int
    phases: deque[JobPhase]

    def __post_init__(self) -> None:
        if len(self.phases) == 0:
            raise ValueError("SimJob must have at least one phase otherwise there is no utility")

    @property
    def no_more_runs(self) -> bool:
        return len(self.phases) == 0

    @property
    def current_phase(self) -> JobPhase | None:
        return None if self.no_more_runs else self.phases[0]

    @property
    def has_active_process(self) -> bool:
        return self.current_phase is not None and self.current_phase == PhaseType.BURST

    def advance_phase(self, duration: int) -> None:
        if self.no_more_runs:
            raise ValueError(f"Cannot run job for {self} because no more runs")
        if duration < 0:
            raise ValueError(f"Cannot run job for {self} because negative duration")
        if duration > self.current_phase.duration:
            raise ValueError(
                "Cannot advance a phase more than the duration of its current phase."
                "\nIf running => we cannot run for longer than our duration"
                "\nIf waiting on IO => event should have been published upon completion of phase not after"
                f"\nDuration given: {duration} for phase {self.current_phase}"
            )
        self.current_phase.duration -= duration
        if self.current_phase.duration == 0:
            self.phases.popleft()
