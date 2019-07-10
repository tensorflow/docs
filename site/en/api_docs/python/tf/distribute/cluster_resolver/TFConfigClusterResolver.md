page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.cluster_resolver.TFConfigClusterResolver

## Class `TFConfigClusterResolver`

Implementation of a ClusterResolver which reads the TF_CONFIG EnvVar.

Inherits From: [`ClusterResolver`](../../../tf/distribute/cluster_resolver/ClusterResolver)

### Aliases:

* Class `tf.compat.v1.distribute.cluster_resolver.TFConfigClusterResolver`
* Class `tf.compat.v2.distribute.cluster_resolver.TFConfigClusterResolver`
* Class `tf.contrib.cluster_resolver.TFConfigClusterResolver`
* Class `tf.contrib.cluster_resolver.python.training.TFConfigClusterResolver`
* Class `tf.distribute.cluster_resolver.TFConfigClusterResolver`



Defined in [`python/distribute/cluster_resolver/tfconfig_cluster_resolver.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    task_type=None,
    task_id=None,
    rpc_layer=None,
    environment=None
)
```

Creates a new TFConfigClusterResolver.


#### Args:


* <b>`task_type`</b>: (String, optional) Overrides the task type specified in the
  TF_CONFIG environment variable.
* <b>`task_id`</b>: (Integer, optional) Overrides the task index specified in the
  TF_CONFIG environment variable.
* <b>`rpc_layer`</b>: (String, optional) Overrides the rpc layer TensorFlow uses.
* <b>`environment`</b>: (String, optional) Overrides the environment TensorFlow
  operates in.



## Properties

<h3 id="environment"><code>environment</code></h3>




<h3 id="rpc_layer"><code>rpc_layer</code></h3>




<h3 id="task_id"><code>task_id</code></h3>




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
    task_id=None,
    rpc_layer=None
)
```

Returns the master address to use when creating a TensorFlow session.


#### Args:


* <b>`task_type`</b>: (String, optional) Overrides and sets the task_type of the
  master.
* <b>`task_id`</b>: (Integer, optional) Overrides and sets the task id of the
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
    task_id=None,
    config_proto=None
)
```






