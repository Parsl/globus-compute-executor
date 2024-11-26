import copy

from globus_compute_executor.executor import GlobusComputeExecutor
from globus_compute_executor.tests.utils import MockExecutor, double


def test_bare_init():
    executor = MockExecutor()
    ex = GlobusComputeExecutor(executor=executor)

    assert not ex.user_endpoint_config
    assert not ex.resource_specification


def test_res_spec_init():
    executor = MockExecutor()
    res_spec = {"num_ranks": 4, "num_nodes": 2}
    ex = GlobusComputeExecutor(executor=executor, resource_specification=res_spec)

    assert not ex.user_endpoint_config
    assert ex.resource_specification == res_spec


def test_res_spec_immutability():
    """Task submission should not modify defaults on the executor"""
    executor = MockExecutor()
    res_spec = {"num_ranks": 4, "num_nodes": 2}
    ex = GlobusComputeExecutor(executor=executor, resource_specification=res_spec)

    for task_res_spec in [
        {"num_ranks": 1, "num_nodes": 1},
        {"num_ranks": 5, "num_nodes": 5},
    ]:
        for user_config in [{"blah": "blah"}, {"foo": "foo"}]:

            res_spec = copy.deepcopy(task_res_spec)
            res_spec["user_endpoint_config"] = user_config
            res, o_res_spec, o_user_config = ex.submit(double, res_spec, 5).result()
            assert task_res_spec == o_res_spec
            assert user_config == o_user_config
