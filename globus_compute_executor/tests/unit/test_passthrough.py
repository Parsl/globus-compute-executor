from concurrent.futures import ThreadPoolExecutor

from globus_compute_executor.executor import GlobusComputeExecutor
from globus_compute_executor.tests.utils import double


def test_passthrough():
    executor = GlobusComputeExecutor(executor=ThreadPoolExecutor())

    for i in range(10):
        fu = executor.submit(double, {}, i)
        assert fu.result() == i * 2

    executor.shutdown()


def test_shutdown():
    executor = GlobusComputeExecutor(executor=ThreadPoolExecutor())

    assert executor.executor._shutdown is False
    executor.shutdown()

    assert executor.executor._shutdown is True
