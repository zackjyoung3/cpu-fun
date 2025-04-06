from dataclasses import dataclass


@dataclass(frozen=True)
class TimeSeed:
    """
    Should be used to gen execution/other times sampling from a normal distribution
    Normal dist much more realistic for our case as Jobs exe times are more likely to be centered about some real mean
    rather than uniformly distributed between min + max run times
    """

    avg_time: int
    std_dev: int


@dataclass(frozen=True)
class SimJobRunSeed:
    num_bursts: int
    burst_seed: TimeSeed
    io_seed: TimeSeed

    @property
    def num_io_reqs(self) -> int:
        """
        When we are having bursts an IO observe that num_io_reqs should always be 1 less than num bursts before end
        under the assumption that we strictly alternate between bursts and IO until job termination
        e.g. Base case 1 Burst: B -> E => 1 burst, 0 i/o
             N+1 Bursts Case: B_0 -> IO_0 -> .... -> B_N -> IO_N -> B_N+1 => N+1 burst, N i/o
        """
        return self.num_bursts - 1


@dataclass(frozen=True)
class SimJobDesc:
    num_runs: int
    req_cycle_seed: TimeSeed
    run_seed: SimJobRunSeed
