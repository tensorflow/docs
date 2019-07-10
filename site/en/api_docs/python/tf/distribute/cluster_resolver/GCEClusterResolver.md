page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.distribute.cluster_resolver.GCEClusterResolver

## Class `GCEClusterResolver`

Cluster Resolver for Google Compute Engine.

Inherits From: [`ClusterResolver`](../../../tf/distribute/cluster_resolver/ClusterResolver)

### Aliases:

* Class `tf.compat.v1.distribute.cluster_resolver.GCEClusterResolver`
* Class `tf.compat.v2.distribute.cluster_resolver.GCEClusterResolver`
* Class `tf.contrib.cluster_resolver.GCEClusterResolver`
* Class `tf.contrib.cluster_resolver.python.training.GCEClusterResolver`
* Class `tf.distribute.cluster_resolver.GCEClusterResolver`



Defined in [`python/distribute/cluster_resolver/gce_cluster_resolver.py`](https://github.com/tensorflow/tensorflow/tree/r1.14/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver.py).

<!-- Placeholder for "Used in" -->

This is an implementation of cluster resolvers for the Google Compute Engine
instance group platform. By specifying a project, zone, and instance group,
this will retrieve the IP address of all the instances within the instance
group and return a Cluster Resolver object suitable for use for distributed
TensorFlow.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    project,
    zone,
    instance_group,
    port,
    task_type='worker',
    task_id=0,
    rpc_layer='grpc',
    credentials='default',
    service=None
)
```

Creates a new GCEClusterResolver object.

This takes in a few parameters and creates a GCEClusterResolver project. It
will then use these parameters to query the GCE API for the IP addresses of
each instance in the instance group.

#### Args:


* <b>`project`</b>: Name of the GCE project.
* <b>`zone`</b>: Zone of the GCE instance group.
* <b>`instance_group`</b>: Name of the GCE instance group.
* <b>`port`</b>: Port of the listening TensorFlow server (default: 8470)
* <b>`task_type`</b>: Name of the TensorFlow job this GCE instance group of VM
  instances belong to.
* <b>`task_id`</b>: The task index for this particular VM, within the GCE
  instance group. In particular, every single instance should be assigned
  a unique ordinal index within an instance group manually so that they
  can be distinguished from each other.
* <b>`rpc_layer`</b>: The RPC layer TensorFlow should use to communicate across
  instances.
* <b>`credentials`</b>: GCE Credentials. If nothing is specified, this defaults to
  GoogleCredentials.get_application_default().
* <b>`service`</b>: The GCE API object returned by the googleapiclient.discovery
  function. (Default: discovery.build('compute', 'v1')). If you specify a
  custom service object, then the credentials parameter will be ignored.


#### Raises:


* <b>`ImportError`</b>: If the googleapiclient is not installed.



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

``` python
cluster_spec()
```

Returns a ClusterSpec object based on the latest instance group info.

This returns a ClusterSpec object for use based on information from the
specified instance group. We will retrieve the information from the GCE APIs
every time this method is called.

#### Returns:

A ClusterSpec containing host information retrieved from GCE.


<h3 id="master"><code>master</code></h3>

``` python
master(
    task_type=None,
    task_id=None,
    rpc_layer=None
)
```




<h3 id="num_accelerators"><code>num_accelerators</code></h3>

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




