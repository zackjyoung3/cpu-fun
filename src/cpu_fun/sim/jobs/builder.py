from collections import deque
from typing import Self

from loguru import logger

from cpu_fun.sim.jobs.job import JobPhase, PhaseType, SimJob


class SimJobBuilder:
    def __init__(self, strict: bool = True):
        """
        init
        :param strict: when True, enforce strict correctness of phases supplied.
        e.g. 2 consecutive phases should never be of the same type.
        If strict => raise ValueError, otherwise => warn
        """
        self._job_id = None
        self._built = False
        self._phases: deque[JobPhase] = deque()
        self._strict = strict

    def with_job_id(self, job_id: int) -> Self:
        self._job_id = job_id
        return self

    def with_phase(self, phase_type: PhaseType, duration: int) -> Self:
        if len(self._phases) > 0 and self._phases[-1].type == phase_type:
            msg = f"Two consecutive phases should never be of the same type, received 2 consecutive {phase_type}"
            if self._strict:
                raise ValueError(msg)
            logger.warning(f"{msg} => joining")
            self._phases[-1].duration += duration
            return self

        new_phase = JobPhase(phase_type, duration)
        self._phases.append(new_phase)
        return self

    def reset(self) -> Self:
        self._built = False
        self._phases.clear()
        self._job_id = None
        return self

    def build(self) -> SimJob:
        if self._job_id is None:
            raise ValueError("Job id was never set")
        if not self._phases:
            raise ValueError("No phases were set")
        if self._built:
            raise ValueError("Job already built")
        self._built = True
        return SimJob(self._job_id, self._phases)
