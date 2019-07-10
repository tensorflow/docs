page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cluster_resolver.GceClusterResolver

## Class `GceClusterResolver`

Inherits From: [`ClusterResolver`](../../../tf/contrib/cluster_resolver/ClusterResolver)



Defined in [`tensorflow/contrib/cluster_resolver/python/training/gce_cluster_resolver.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/cluster_resolver/python/training/gce_cluster_resolver.py).

Cluster Resolver for Google Compute Engine.

This is an implementation of cluster resolvers for the Google Compute Engine
instance group platform. By specifying a project, zone, and instance group,
this will retrieve the IP address of all the instances within the instance
group and return a Cluster Resolver object suitable for use for distributed
TensorFlow.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    project,
    zone,
    instance_group,
    port,
    job_name='worker',
    credentials='default',
    service=None
)
```

Creates a new GceClusterResolver object.

This takes in a few parameters and creates a GceClusterResolver project. It
will then use these parameters to query the GCE API for the IP addresses of
each instance in the instance group.

#### Args:

* <b>`project`</b>: Name of the GCE project
* <b>`zone`</b>: Zone of the GCE instance group
* <b>`instance_group`</b>: Name of the GCE instance group
* <b>`port`</b>: Port of the listening TensorFlow server (default: 8470)
* <b>`job_name`</b>: Name of the TensorFlow job this set of instances belongs to
* <b>`credentials`</b>: GCE Credentials. If nothing is specified, this defaults to
    GoogleCredentials.get_application_default()
* <b>`service`</b>: The GCE API object returned by the googleapiclient.discovery
    function. (Default: discovery.build('compute', 'v1')). If you specify a
    custom service object, then the credentials parameter will be ignored.


#### Raises:

* <b>`ImportError`</b>: If the googleapiclient is not installed.

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
master()
```





