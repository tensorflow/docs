page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cluster_resolver.GceClusterResolver

## Class `GceClusterResolver`

Inherits From: [`ClusterResolver`](../../../tf/contrib/cluster_resolver/ClusterResolver)

### Aliases:

* Class `tf.contrib.cluster_resolver.GceClusterResolver`
* Class `tf.contrib.cluster_resolver.python.training.GceClusterResolver`



Defined in [`tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/distribute/cluster_resolver/gce_cluster_resolver.py).

Cluster Resolver for Google Compute Engine.

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
    task_index=0,
    rpc_layer='grpc',
    credentials='default',
    service=None
)
```

Creates a new GceClusterResolver object.

This takes in a few parameters and creates a GceClusterResolver project. It
will then use these parameters to query the GCE API for the IP addresses of
each instance in the instance group.

#### Args:

* <b>`project`</b>: Name of the GCE project.
* <b>`zone`</b>: Zone of the GCE instance group.
* <b>`instance_group`</b>: Name of the GCE instance group.
* <b>`port`</b>: Port of the listening TensorFlow server (default: 8470)
* <b>`task_type`</b>: Name of the TensorFlow job this GCE instance group of VM
    instances belong to.
* <b>`task_index`</b>: The task index for this particular VM, within the GCE
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

For users in the GCE environment, the environment property is always an
empty string, and Google users will not use this ClusterResolver for running
on internal systems.

<h3 id="rpc_layer"><code>rpc_layer</code></h3>



<h3 id="task_index"><code>task_index</code></h3>



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



