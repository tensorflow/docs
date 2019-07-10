page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cluster_resolver.ClusterResolver

## Class `ClusterResolver`



### Aliases:

* Class `tf.contrib.cluster_resolver.ClusterResolver`
* Class `tf.contrib.cluster_resolver.python.training.ClusterResolver`



Defined in [`tensorflow/python/distribute/cluster_resolver/cluster_resolver.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py).

Abstract class for all implementations of ClusterResolvers.

This defines the skeleton for all implementations of ClusterResolvers.
ClusterResolvers are a way for TensorFlow to communicate with various cluster
management systems (e.g. GCE, AWS, etc...).

By letting TensorFlow communicate with these systems, we will be able to
automatically discover and resolve IP addresses for various TensorFlow
workers. This will eventually allow us to automatically recover from
underlying machine failures and scale TensorFlow worker clusters up and down.

Note to Implementors: In addition to these abstract methods, you must also
implement the task_type, task_index, and rpc_layer attributes. You may choose
to implement them either as properties with getters or setters or directly
set the attributes.

- task_type is the name of the server's current named job (e.g. 'worker',
   'ps' in a distributed parameterized training job).
- task_index is the ordinal index of the server within the task type.
- rpc_layer is the protocol used by TensorFlow to communicate with other
    TensorFlow servers in a distributed environment.

## Properties

<h3 id="environment"><code>environment</code></h3>

Returns the current environment which TensorFlow is running in.



## Methods

<h3 id="cluster_spec"><code>cluster_spec</code></h3>

``` python
cluster_spec()
```

Retrieve the current state of the cluster and returns a ClusterSpec.

#### Returns:

  A ClusterSpec representing the state of the cluster at the moment this
  function is called.

Implementors of this function must take care in ensuring that the
ClusterSpec returned is up-to-date at the time of calling this function.
This usually means retrieving the information from the underlying cluster
management system every time this function is invoked and reconstructing
a cluster_spec, rather than attempting to cache anything.

<h3 id="master"><code>master</code></h3>

``` python
master(
    task_type=None,
    task_index=None,
    rpc_layer=None
)
```

Retrieves the name or URL of the session master.

#### Args:

* <b>`task_type`</b>: (Optional) The type of the TensorFlow task of the master.
* <b>`task_index`</b>: (Optional) The index of the TensorFlow task of the master.
* <b>`rpc_layer`</b>: (Optional) The RPC protocol for the given cluster.


#### Returns:

  The name or URL of the session master.

Implementors of this function must take care in ensuring that the master
returned is up-to-date at the time to calling this function. This usually
means retrieving the master every time this function is invoked.

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



