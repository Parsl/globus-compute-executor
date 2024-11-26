from concurrent.futures import Future


def double(x):
    return x * 2


class MockExecutor:

    def __init__(self, user_endpoint_config=None, resource_specification=None):
        self.user_endpoint_config = user_endpoint_config
        self.resource_specification = resource_specification

    def submit(self, func, *args, **kwargs):
        future = Future()
        try:
            result = func(*args, **kwargs)
            # This will return the executor submit state
            future.set_result(
                (result, self.resource_specification, self.user_endpoint_config)
            )
        except Exception as e:
            future.set_exception(exception=e)
        return future
