# cpu-fun

## Motivation
Simulate the execution of processes on the CPU via a simple scheduler virtualization
- Covered these in college, but never implemented simulation for anything like CFS, MLFQ or Lottery
- Revisit simulation with my own design after being in industry


## Schedulers to Implement
### Preemptive Schedulers
- CFS
- MLFQ
- SRTF
- Round Robin
### Non-preemptive Schedulers
- FIFO
- SJF
### Proportional Share Scheduling
- Lottery
- CFS (dup)

## Metrics to capture
Turnaround Time = Completion Time - Arrival Time
Waiting Time = Turnaround Time - Burst Time
Response Time = First Scheduled Time - Arrival Time


## Design Paradigm
- I wanted my simulation to present as if there was a real scheduling scenario.
- Thus, as much as possible, I have tried to maintain a strict separation of concerns between that which is...
  - more properly expressed in the kernel + the scheduler reacts to events on the fly
  - more properly expressed in the simulation + we should propagate a simulation event to the scheduler