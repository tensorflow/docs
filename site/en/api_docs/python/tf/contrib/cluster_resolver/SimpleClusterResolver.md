page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cluster_resolver.SimpleClusterResolver

## Class `SimpleClusterResolver`

Inherits From: [`ClusterResolver`](../../../tf/contrib/cluster_resolver/ClusterResolver)

### Aliases:

* Class `tf.contrib.cluster_resolver.SimpleClusterResolver`
* Class `tf.contrib.cluster_resolver.python.training.SimpleClusterResolver`



Defined in [`tensorflow/python/distribute/cluster_resolver/cluster_resolver.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py).

Simple implementation of ClusterResolver that accepts a ClusterSpec.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    cluster_spec,
    master='',
    task_type=None,
    task_index=None,
    environment='',
    num_accelerators=0,
    rpc_layer=None
)
```

Creates a SimpleClusterResolver from a ClusterSpec.



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

Returns the ClusterSpec passed into the constructor.

<h3 id="master"><code>master</code></h3>

``` python
master(
    task_type=None,
    task_index=None,
    rpc_layer=None
)
```

Returns the master address to use when creating a session.

#### Args:

* <b>`task_type`</b>: (Optional) The type of the TensorFlow task of the master.
* <b>`task_index`</b>: (Optional) The index of the TensorFlow task of the master.
* <b>`rpc_layer`</b>: (Optional) The RPC used by distributed TensorFlow.


#### Returns:

  The name or URL of the session master.

If a task_type and task_index is given, this will override the `master`
string passed into the initialization function.

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

The SimpleClusterResolver does not do automatic detection of accelerators,
so a TensorFlow session will never be created, and thus all arguments are
unused and we simply return whatever was passed in when this object was
initialized.

#### Args:

* <b>`task_type`</b>: Unused.
* <b>`task_index`</b>: Unused.
* <b>`accelerator_type`</b>: Unused.
* <b>`config_proto`</b>: Unused.



