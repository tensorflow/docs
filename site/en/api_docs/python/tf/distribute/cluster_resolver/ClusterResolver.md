page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.cluster_resolver.ClusterResolver


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L67-L178">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `ClusterResolver`

Abstract class for all implementations of ClusterResolvers.



### Aliases:

* Class `tf.compat.v1.distribute.cluster_resolver.ClusterResolver`
* Class `tf.compat.v2.distribute.cluster_resolver.ClusterResolver`


<!-- Placeholder for "Used in" -->

This defines the skeleton for all implementations of ClusterResolvers.
ClusterResolvers are a way for TensorFlow to communicate with various cluster
management systems (e.g. GCE, AWS, etc...).

By letting TensorFlow communicate with these systems, we will be able to
automatically discover and resolve IP addresses for various TensorFlow
workers. This will eventually allow us to automatically recover from
underlying machine failures and scale TensorFlow worker clusters up and down.

Note to Implementors: In addition to these abstract methods, you must also
implement the task_type, task_id, and rpc_layer attributes. You may choose
to implement them either as properties with getters or setters or directly
set the attributes.

- task_type is the name of the server's current named job (e.g. 'worker',
   'ps' in a distributed parameterized training job).
- task_id is the ordinal index of the server within the task type.
- rpc_layer is the protocol used by TensorFlow to communicate with other
    TensorFlow servers in a distributed environment.

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L91-L105">View source</a>

``` python
cluster_spec()
```

Retrieve the current state of the cluster and return a ClusterSpec.


#### Returns:

A ClusterSpec representing the state of the cluster at the moment this
function is called.


Implementors of this function must take care in ensuring that the
ClusterSpec returned is up-to-date at the time of calling this function.
This usually means retrieving the information from the underlying cluster
management system every time this function is invoked and reconstructing
a cluster_spec, rather than attempting to cache anything.

<h3 id="master"><code>master</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L107-L123">View source</a>

``` python
master(
    task_type=None,
    task_id=None,
    rpc_layer=None
)
```

Retrieves the name or URL of the session master.


#### Args:


* <b>`task_type`</b>: (Optional) The type of the TensorFlow task of the master.
* <b>`task_id`</b>: (Optional) The index of the TensorFlow task of the master.
* <b>`rpc_layer`</b>: (Optional) The RPC protocol for the given cluster.


#### Returns:

The name or URL of the session master.


Implementors of this function must take care in ensuring that the master
returned is up-to-date at the time to calling this function. This usually
means retrieving the master every time this function is invoked.

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
