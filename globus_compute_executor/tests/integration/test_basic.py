import os

from globus_compute_sdk import Executor

from globus_compute_executor import GlobusComputeExecutor
from globus_compute_executor.tests.utils import double


def test_simple():
    endpoint_id = os.environ["GLOBUS_COMPUTE_ENDPOINT"]

    executor = GlobusComputeExecutor(executor=Executor(endpoint_id=endpoint_id))

    futures = {}
    for i in range(5):
        future = executor.submit(double, {}, i)
        futures[i] = future

    for key in futures:
        assert futures[key].result(timeout=120) == key * 2
