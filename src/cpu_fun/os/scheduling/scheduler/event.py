from dataclasses import dataclass
from enum import StrEnum

from cpu_fun.os.scheduling.process import Process


class EventType(StrEnum):
    PROC_ARRIVED = "proc_arrived"
    PROC_REQ_IO = "proc_req_io"
    PROC_REC_IO = "proc_rec_io"
    PROC_COMPLETE = "proc_complete"


@dataclass(frozen=True)
class Event:
    type: EventType
    associated_process: Process
