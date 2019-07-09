page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cluster_resolver.KubernetesClusterResolver

## Class `KubernetesClusterResolver`

Inherits From: [`ClusterResolver`](../../../tf/contrib/cluster_resolver/ClusterResolver)

### Aliases:

* Class `tf.contrib.cluster_resolver.KubernetesClusterResolver`
* Class `tf.contrib.cluster_resolver.python.training.KubernetesClusterResolver`



Defined in [`tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver.py).

Cluster Resolver for Kubernetes.

This is an implementation of cluster resolvers for Kubernetes. When given the
the Kubernetes namespace and label selector for pods, we will retrieve the
pod IP addresses of all running pods matching the selector, and return a
ClusterSpec based on that information.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    job_to_label_mapping=None,
    tf_server_port=8470,
    rpc_layer='grpc',
    override_client=None
)
```

Initializes a new KubernetesClusterResolver.

This initializes a new Kubernetes Cluster Resolver. The Cluster Resolver
will attempt to talk to the Kubernetes master to retrieve all the instances
of pods matching a label selector.

#### Args:

* <b>`job_to_label_mapping`</b>: A mapping of TensorFlow jobs to label selectors.
    This allows users to specify many TensorFlow jobs in one Cluster
    Resolver, and each job can have pods belong with different label
    selectors. For example, a sample mapping might be

    ```
    {'worker': ['job-name=worker-cluster-a', 'job-name=worker-cluster-b'],
     'ps': ['job-name=ps-1', 'job-name=ps-2']}
    ```
* <b>`tf_server_port`</b>: The port the TensorFlow server is listening on.
* <b>`rpc_layer`</b>: (Optional) The RPC layer TensorFlow should use to communicate
    between tasks in Kubernetes. Defaults to 'grpc'.
* <b>`override_client`</b>: The Kubernetes client (usually automatically retrieved
    using `from kubernetes import client as k8sclient`). If you pass this
    in, you are responsible for setting Kubernetes credentials manually.


#### Raises:

* <b>`ImportError`</b>: If the Kubernetes Python client is not installed and no
    `override_client` is passed in.
* <b>`RuntimeError`</b>: If autoresolve_task is not a boolean or a callable.



## Properties

<h3 id="environment"><code>environment</code></h3>

Returns the current environment which TensorFlow is running in.

For users in the Cloud environment, the environment property is always an
empty string, and Google users will not use this ClusterResolver for running
on internal systems.



## Methods

<h3 id="cluster_spec"><code>cluster_spec</code></h3>

``` python
cluster_spec()
```

Returns a ClusterSpec object based on the latest info from Kubernetes.

We retrieve the information from the Kubernetes master every time this
method is called.

#### Returns:

A ClusterSpec containing host information returned from Kubernetes.


#### Raises:

* <b>`RuntimeError`</b>: If any of the pods returned by the master is not in the
    `Running` phase.

<h3 id="master"><code>master</code></h3>

``` python
master(
    task_type=None,
    task_index=None,
    rpc_layer=None
)
```

Returns the master address to use when creating a session.

You must have set the task_type and task_index object properties before
calling this function, or pass in the `task_type` and `task_index`
parameters when using this function. If you do both, the function parameters
will override the object properties.

#### Args:

* <b>`task_type`</b>: (Optional) The type of the TensorFlow task of the master.
* <b>`task_index`</b>: (Optional) The index of the TensorFlow task of the master.
* <b>`rpc_layer`</b>: (Optional) The RPC protocol for the given cluster.


#### Returns:

The name or URL of the session master.

<h3 id="num_accelerators"><code>num_accelerators</code></h3>

``` python
num_accelerators(
    task_type=None,
    task_index=None,
    accelerator_type='GPU',
    config_proto=None
)
```

Returns the number of accelerator cores per worker.

This returns the number of accelerator cores (such as GPUs and TPUs)
available per worker. If workers only has CPU cores available, then this
should return 0. This method will query the master for this information
if it is not otherwise known.

Optionally, we allow callers to specify the task_type, task_index, and
rpc_layer, if they want to target a specific TensorFlow process to query
the number of accelerators. This is to support heterogenous environments,
where the number of accelerators cores per host is different.

#### Args:

* <b>`task_type`</b>: (Optional) The type of the TensorFlow task of the machine we
    want to query.
* <b>`task_index`</b>: (Optional) The index of the TensorFlow task of the machine we
    want to query.
* <b>`accelerator_type`</b>: (Optional) The type of accelerator we are trying to
    query (defaults to 'GPU').
* <b>`config_proto`</b>: (Optional) Configuration for starting a new session to
    query how many accelerator cores it has.



