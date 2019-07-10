page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.cluster_resolver.SlurmClusterResolver

## Class `SlurmClusterResolver`

Cluster Resolver for system with Slurm workload manager.

Inherits From: [`ClusterResolver`](../../../tf/distribute/cluster_resolver/ClusterResolver)

### Aliases:

* Class `tf.compat.v1.distribute.cluster_resolver.SlurmClusterResolver`
* Class `tf.compat.v2.distribute.cluster_resolver.SlurmClusterResolver`
* Class `tf.contrib.cluster_resolver.SlurmClusterResolver`
* Class `tf.contrib.cluster_resolver.python.training.SlurmClusterResolver`
* Class `tf.distribute.cluster_resolver.SlurmClusterResolver`



Defined in [`python/distribute/cluster_resolver/slurm_cluster_resolver.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/distribute/cluster_resolver/slurm_cluster_resolver.py).

<!-- Placeholder for "Used in" -->

This is an implementation of cluster resolvers for Slurm clusters. This allows
the specification of jobs and task counts, number of tasks per node, number of
GPUs on each node and number of GPUs for each task, It retrieves system
attributes by Slurm environment variables, resolves allocated computing node
names, construct a cluster and return a Cluster Resolver object which an be
use for distributed TensorFlow.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    jobs,
    port_base=8888,
    gpus_per_node=1,
    gpus_per_task=1,
    tasks_per_node=None,
    auto_set_gpu=True,
    rpc_layer='grpc'
)
```

Creates a new SlurmClusterResolver object.

This takes in parameters and creates a SlurmClusterResolver object. It uses
those parameters to check which nodes will processes reside and resolves
their hostnames. With the number of the GPUs on each node and number of GPUs
for each task it offsets the port number for each processes and allocate
GPUs to tasks by setting environment variables. The resolver currently
supports homogeneous tasks and default Slurm process allocation.

#### Args:


* <b>`jobs`</b>: Dictionary with job names as key and number of tasks in the job as
  value
* <b>`port_base`</b>: The first port number to start with for processes on a node.
* <b>`gpus_per_node`</b>: Number of GPUs available on each node.
* <b>`gpus_per_task`</b>: Number of GPUs to be used for each task.
* <b>`tasks_per_node`</b>: Number of tasks to run on each node, if not set defaults
  to Slurm's output environment variable SLURM_NTASKS_PER_NODE.
* <b>`auto_set_gpu`</b>: Set the visible CUDA devices automatically while resolving
  the cluster by setting CUDA_VISIBLE_DEVICES environment variable.
  Defaults to True.
* <b>`rpc_layer`</b>: (Optional) The protocol TensorFlow uses to communicate between
  nodes. Defaults to 'grpc'.


#### Returns:

A ClusterResolver object which can be used with distributed TensorFlow.



#### Raises:


* <b>`RuntimeError`</b>: If requested more GPUs per node then available or requested
more tasks then assigned tasks.



## Properties

<h3 id="environment"><code>environment</code></h3>

Returns the current environment which TensorFlow is running in.

There are two possible return values, "google" (when TensorFlow is running
in a Google-internal environment) or an empty string (when TensorFlow is
running elsewhere).

If you are implementing a ClusterResolver that works in both the Google
environment and the open-source world (for instance, a TPU ClusterResolver
or similar), you will have to return the appropriate string depending on the
environment, which you will have to detect.

Otherwise, if you are implementing a ClusterResolver that will only work
in open-source TensorFlow, you do not need to implement this property.



## Methods

<h3 id="cluster_spec"><code>cluster_spec</code></h3>

``` python
cluster_spec()
```

Returns a ClusterSpec object based on the latest instance group info.

This returns a ClusterSpec object for use based on information from the
specified initialization parameters and Slurm environment variables. The
cluster specification is resolved each time this function is called. The
resolver extract hostnames of nodes by scontrol and pack tasks in that
order until a node a has number of tasks that is equal to specification.
GPUs on nodes are allocated to tasks by specification through setting
CUDA_VISIBLE_DEVICES environment variable.

#### Returns:

A ClusterSpec containing host information retrieved from Slurm's
  environment variables.


<h3 id="get_task_info"><code>get_task_info</code></h3>

``` python
get_task_info()
```

Returns job name and task_id for the process which calls this.

This returns the job name and task index for the process which calls this
function according to its rank and cluster specification. The job name and
task index are set after a cluster is constructed by cluster_spec otherwise
defaults to None.

#### Returns:

A string specifying job name the process belongs to and an integner
  specifying the task index the process belongs to in that job.


<h3 id="master"><code>master</code></h3>

``` python
master(
    task_type=None,
    task_id=None,
    rpc_layer=None
)
```

Returns the master string for connecting to a TensorFlow master.


#### Args:


* <b>`task_type`</b>: (Optional) Overrides the default auto-selected task type.
* <b>`task_id`</b>: (Optional) Overrides the default auto-slected task index.
* <b>`rpc_layer`</b>: (Optional) Overrides the default RPC protocol TensorFlow uses
  to communicate across nodes.


#### Returns:

A connection string for connecting to a TensorFlow master.


<h3 id="num_accelerators"><code>num_accelerators</code></h3>

``` python
num_accelerators(
    task_type=None,
    task_id=None,
    config_proto=None
)
```






