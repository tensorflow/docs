page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.cluster_resolver.TFConfigClusterResolver


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py#L52-L177">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TFConfigClusterResolver`

Implementation of a ClusterResolver which reads the TF_CONFIG EnvVar.

Inherits From: [`ClusterResolver`](../../../tf/distribute/cluster_resolver/ClusterResolver)

### Aliases:

* Class `tf.compat.v1.distribute.cluster_resolver.TFConfigClusterResolver`
* Class `tf.compat.v2.distribute.cluster_resolver.TFConfigClusterResolver`


<!-- Placeholder for "Used in" -->

This is an implementation of cluster resolvers when using TF_CONFIG to set
information about the cluster. The cluster spec returned will be
initialized from the TF_CONFIG environment variable.

<h2 id="__init__"><code>__init__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py#L60-L79">View source</a>

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

<h3 id="rpc_layer"><code>rpc_layer</code></h3>




<h3 id="task_id"><code>task_id</code></h3>




<h3 id="task_type"><code>task_type</code></h3>






## Methods

<h3 id="cluster_spec"><code>cluster_spec</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py#L129-L138">View source</a>

``` python
cluster_spec()
```

Returns a ClusterSpec based on the TF_CONFIG environment variable.


#### Returns:

A ClusterSpec with information from the TF_CONFIG environment variable.


<h3 id="master"><code>master</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py#L140-L177">View source</a>

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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/tree/r2.0/tensorflow/python/distribute/cluster_resolver/tfconfig_cluster_resolver.py#L120-L127">View source</a>

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
