page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.cluster_resolver.SimpleClusterResolver

## Class `SimpleClusterResolver`

Simple implementation of ClusterResolver that accepts a ClusterSpec.

Inherits From: [`ClusterResolver`](../../../tf/distribute/cluster_resolver/ClusterResolver)

### Aliases:

* Class `tf.compat.v1.distribute.cluster_resolver.SimpleClusterResolver`
* Class `tf.compat.v2.distribute.cluster_resolver.SimpleClusterResolver`
* Class `tf.contrib.cluster_resolver.SimpleClusterResolver`
* Class `tf.contrib.cluster_resolver.python.training.SimpleClusterResolver`
* Class `tf.distribute.cluster_resolver.SimpleClusterResolver`



Defined in [`python/distribute/cluster_resolver/cluster_resolver.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py).

<!-- Placeholder for "Used in" -->


<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    cluster_spec,
    master='',
    task_type=None,
    task_id=None,
    environment='',
    num_accelerators=None,
    rpc_layer=None
)
```

Creates a SimpleClusterResolver from a ClusterSpec.




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

Returns the ClusterSpec passed into the constructor.


<h3 id="master"><code>master</code></h3>

``` python
master(
    task_type=None,
    task_id=None,
    rpc_layer=None
)
```

Returns the master address to use when creating a session.


#### Args:


* <b>`task_type`</b>: (Optional) The type of the TensorFlow task of the master.
* <b>`task_id`</b>: (Optional) The index of the TensorFlow task of the master.
* <b>`rpc_layer`</b>: (Optional) The RPC used by distributed TensorFlow.


#### Returns:

The name or URL of the session master.


If a task_type and task_id is given, this will override the `master`
string passed into the initialization function.

<h3 id="num_accelerators"><code>num_accelerators</code></h3>

``` python
num_accelerators(
    task_type=None,
    task_id=None,
    config_proto=None
)
```

Returns the number of accelerator cores per worker.

The SimpleClusterResolver does not do automatic detection of accelerators,
so a TensorFlow session will never be created, and thus all arguments are
unused and we simply assume that the type of accelerator is a GPU and return
the value in provided to us in the constructor.

#### Args:


* <b>`task_type`</b>: Unused.
* <b>`task_id`</b>: Unused.
* <b>`config_proto`</b>: Unused.



