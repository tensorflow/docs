page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cluster_resolver.TFConfigClusterResolver

## Class `TFConfigClusterResolver`

Inherits From: [`ClusterResolver`](../../../tf/contrib/cluster_resolver/ClusterResolver)

### Aliases:

* Class `tf.contrib.cluster_resolver.TFConfigClusterResolver`
* Class `tf.contrib.cluster_resolver.python.training.TFConfigClusterResolver`



Defined in [`tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py).

Implementation of a ClusterResolver which reads the TF_CONFIG EnvVar.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    task_type=None,
    task_index=None,
    rpc_layer=None,
    environment=None
)
```

Creates a new TFConfigClusterResolver.

#### Args:

* <b>`task_type`</b>: (String, optional) Overrides the task type specified in the
    TF_CONFIG environment variable.
* <b>`task_index`</b>: (Integer, optional) Overrides the task index specified in the
    TF_CONFIG environment variable.
* <b>`rpc_layer`</b>: (String, optional) Overrides the rpc layer TensorFlow uses.
* <b>`environment`</b>: (String, optional) Overrides the environment TensorFlow
    operates in.



## Properties

<h3 id="environment"><code>environment</code></h3>

Returns the current environment which TensorFlow is running in.

<h3 id="rpc_layer"><code>rpc_layer</code></h3>



<h3 id="task_index"><code>task_index</code></h3>



<h3 id="task_type"><code>task_type</code></h3>





## Methods

<h3 id="cluster_spec"><code>cluster_spec</code></h3>

``` python
cluster_spec()
```

Returns a ClusterSpec based on the TF_CONFIG environment variable.

#### Returns:

A ClusterSpec with information from the TF_CONFIG environment variable.

<h3 id="master"><code>master</code></h3>

``` python
master(
    task_type=None,
    task_index=None,
    rpc_layer=None
)
```

Returns the master address to use when creating a TensorFlow session.

#### Args:

* <b>`task_type`</b>: (String, optional) Overrides and sets the task_type of the
    master.
* <b>`task_index`</b>: (Integer, optional) Overrides and sets the task id of the
    master.
* <b>`rpc_layer`</b>: (String, optional) Overrides and sets the protocol over which
    TensorFlow nodes communicate with each other.


#### Returns:

The address of the master.


#### Raises:

* <b>`RuntimeError`</b>: If the task_type or task_id is not specified and the
    `TF_CONFIG` environment variable does not contain a task section.

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



