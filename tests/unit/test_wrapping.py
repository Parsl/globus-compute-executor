from unittest import mock

from globus_compute_sdk import Executor

from globus_compute_executor.executor import GlobusComputeExecutor


def double(x):
    return x * 2


def test_bare_init():
    executor = mock.Mock(spec=Executor)
    ex = GlobusComputeExecutor(executor=executor)

    assert not ex.user_endpoint_config
    assert not ex.resource_specification


def test_res_spec_init():
    executor = mock.Mock(spec=Executor)
    res_spec = {"num_ranks": 4, "num_nodes": 2}
    ex = GlobusComputeExecutor(executor=executor, resource_specification=res_spec)

    assert not ex.user_endpoint_config
    assert ex.resource_specification == res_spec
