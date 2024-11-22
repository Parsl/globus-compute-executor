# Globus Compute Executor

Globus Compute Executor is a plugin adapter for Parsl that enables enables flexible,
scalable, and high performance remote function execution. This enables Parsl to run
comples Scientific Workflows at scale from laptops to campus clusters, clouds, and
supercomputers.

This module is a thin wrapper over Globus Compute SDK's [executor interface]
(https://globus-compute.readthedocs.io/en/latest/executor.html),  which is used
for task submission via Globus Compute.

To manage your own compute endpoints where tasks execute , use the companion
[Globus Compute Endpoint](https://pypi.org/project/globus-compute-endpoint/) package.