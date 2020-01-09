page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.cluster_resolver.KubernetesClusterResolver


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver.py#L35-L158">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `KubernetesClusterResolver`

ClusterResolver for Kubernetes.

Inherits From: [`ClusterResolver`](../../../tf/distribute/cluster_resolver/ClusterResolver)

### Aliases:

* Class `tf.compat.v1.distribute.cluster_resolver.KubernetesClusterResolver`
* Class `tf.compat.v2.distribute.cluster_resolver.KubernetesClusterResolver`


<!-- Placeholder for "Used in" -->

This is an implementation of cluster resolvers for Kubernetes. When given the
the Kubernetes namespace and label selector for pods, we will retrieve the
pod IP addresses of all running pods matching the selector, and return a
ClusterSpec based on that information.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver.py#L44-L94">View source</a>

``` python
__init__(
    job_to_label_mapping=None,
    tf_server_port=8470,
    rpc_layer='grpc',
    override_client=None
)
```

Initializes a new KubernetesClusterResolver.

This initializes a new Kubernetes ClusterResolver. The ClusterResolver
will attempt to talk to the Kubernetes master to retrieve all the instances
of pods matching a label selector.

#### Args:


* <b>`job_to_label_mapping`</b>: A mapping of TensorFlow jobs to label selectors.
  This allows users to specify many TensorFlow jobs in one Cluster
  Resolver, and each job can have pods belong with different label
  selectors. For example, a sample mapping might be

>     {'worker': ['job-name=worker-cluster-a', 'job-name=worker-cluster-b'],
>      'ps': ['job-name=ps-1', 'job-name=ps-2']}
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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver.py#L122-L158">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver.py#L96-L120">View source</a>

``` python
master(
    task_type=None,
    task_id=None,
    rpc_layer=None
)
```

Returns the master address to use when creating a session.

You must have set the task_type and task_id object properties before
calling this function, or pass in the `task_type` and `task_id`
parameters when using this function. If you do both, the function parameters
will override the object properties.

#### Args:


* <b>`task_type`</b>: (Optional) The type of the TensorFlow task of the master.
* <b>`task_id`</b>: (Optional) The index of the TensorFlow task of the master.
* <b>`rpc_layer`</b>: (Optional) The RPC protocol for the given cluster.


#### Returns:

The name or URL of the session master.


<h3 id="num_accelerators"><code>num_accelerators</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L125-L160">View source</a>

``` python
num_accelerators(
    task_type=None,
    task_id=None,
    config_proto=None
)
```

Returns the number of accelerator cores per worker.

This returns the number of accelerator cores (such as GPUs and TPUs)
available per worker.

Optionally, we allow callers to specify the task_type, and task_id, for
if they want to target a specific TensorFlow process to query
the number of accelerators. This is to support heterogenous environments,
where the number of accelerators cores per host is different.

#### Args:


* <b>`task_type`</b>: (Optional) The type of the TensorFlow task of the machine we
  want to query.
* <b>`task_id`</b>: (Optional) The index of the TensorFlow task of the machine we
  want to query.
* <b>`config_proto`</b>: (Optional) Configuration for starting a new session to
  query how many accelerator cores it has.


#### Returns:

A map of accelerator types to number of cores.
