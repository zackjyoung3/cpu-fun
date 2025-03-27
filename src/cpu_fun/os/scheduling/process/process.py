from dataclasses import dataclass

from cpu_fun.os.scheduling.process.state import ProcessState


@dataclass
class Process:
    id: int
    job_id: int
    state: ProcessState
