page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cluster_resolver.UnionClusterResolver

## Class `UnionClusterResolver`

Inherits From: [`ClusterResolver`](../../../tf/contrib/cluster_resolver/ClusterResolver)

### Aliases:

* Class `tf.contrib.cluster_resolver.UnionClusterResolver`
* Class `tf.contrib.cluster_resolver.python.training.UnionClusterResolver`



Defined in [`tensorflow/python/distribute/cluster_resolver/cluster_resolver.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py).

Performs a union on underlying ClusterResolvers.

This class performs a union given two or more existing ClusterResolvers. It
merges the underlying ClusterResolvers, and returns one unified ClusterSpec
when cluster_spec is called. The details of the merge function is
documented in the cluster_spec function.

For additional Cluster Resolver properties such as task type, task index,
rpc layer, environment, etc..., we will return the value from the first
ClusterResolver in the union.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    *args,
    **kwargs
)
```

Initializes a UnionClusterResolver with other ClusterResolvers.

#### Args:

* <b>`*args`</b>: `ClusterResolver` objects to be unionized.
* <b>`**kwargs`</b>:     rpc_layer - (Optional) Override value for the RPC layer used by
      TensorFlow.
    task_type - (Optional) Override value for the current task type.
    task_index - (Optional) Override value for the current task index.


#### Raises:

* <b>`TypeError`</b>: If any argument is not a subclass of `ClusterResolvers`.
* <b>`ValueError`</b>: If there are no arguments passed.



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

Returns a union of all the ClusterSpecs from the ClusterResolvers.

#### Returns:

A ClusterSpec containing host information merged from all the underlying
ClusterResolvers.


#### Raises:

* <b>`KeyError`</b>: If there are conflicting keys detected when merging two or
  more dictionaries, this exception is raised.

Note: If there are multiple ClusterResolvers exposing ClusterSpecs with the
same job name, we will merge the list/dict of workers.

If *all* underlying ClusterSpecs expose the set of workers as lists, we will
concatenate the lists of workers, starting with the list of workers from
the first ClusterResolver passed into the constructor.

If *any* of the ClusterSpecs expose the set of workers as a dict, we will
treat all the sets of workers as dicts (even if they are returned as lists)
and will only merge them into a dict if there is no conflicting keys. If
there is a conflicting key, we will raise a `KeyError`.

<h3 id="master"><code>master</code></h3>

``` python
master(
    task_type=None,
    task_index=None,
    rpc_layer=None
)
```

Returns the master address to use when creating a session.

This usually returns the master from the first ClusterResolver passed in,
but you can override this by specifying the task_type and task_index.

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



