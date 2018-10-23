

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.cluster_resolver.TPUClusterResolver

## Class `TPUClusterResolver`

Inherits From: [`ClusterResolver`](../../../tf/contrib/cluster_resolver/ClusterResolver)



Defined in [`tensorflow/contrib/cluster_resolver/python/training/tpu_cluster_resolver.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.6/tensorflow/contrib/cluster_resolver/python/training/tpu_cluster_resolver.py).

Cluster Resolver for Google Cloud TPUs.

This is an implementation of cluster resolvers for the Google Cloud TPU
service. As Cloud TPUs are in alpha, you will need to specify a API definition
file for this to consume, in addition to a list of Cloud TPUs in your Google
Cloud Platform project.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    tpu_names,
    zone=None,
    project=None,
    job_name='tpu_worker',
    credentials='default',
    service=None
)
```

Creates a new TPUClusterResolver object.

The ClusterResolver will then use the parameters to query the Cloud TPU APIs
for the IP addresses and ports of each Cloud TPU listed.

#### Args:

* <b>`tpu_names`</b>: A list of names of the target Cloud TPUs.
* <b>`zone`</b>: Zone where the TPUs are located. If omitted or empty, we will assume
    that the zone of the TPU is the same as the zone of the GCE VM, which we
    will try to discover from the GCE metadata service.
* <b>`project`</b>: Name of the GCP project containing Cloud TPUs. If omitted or
    empty, we will try to discover the project name of the GCE VM from the
    GCE metadata service.
* <b>`job_name`</b>: Name of the TensorFlow job the TPUs belong to.
* <b>`credentials`</b>: GCE Credentials. If None, then we use default credentials
    from the oauth2client
* <b>`service`</b>: The GCE API object returned by the googleapiclient.discovery
    function. If you specify a custom service object, then the credentials
    parameter will be ignored.


#### Raises:

* <b>`ImportError`</b>: If the googleapiclient is not installed.

<h3 id="cluster_spec"><code>cluster_spec</code></h3>

``` python
cluster_spec()
```

Returns a ClusterSpec object based on the latest TPU information.

We retrieve the information from the GCE APIs every time this method is
called.

#### Returns:

A ClusterSpec containing host information returned from Cloud TPUs.

<h3 id="get_master"><code>get_master</code></h3>

``` python
get_master()
```

Get the ClusterSpec grpc master path.

This returns the grpc path (grpc://1.2.3.4:8470) of first instance in the
ClusterSpec returned by the cluster_spec function. This is suitable for use
for the `master` argument in tf.Session() when you are using one TPU.

#### Returns:

string, the grpc path of the first instance in the ClusterSpec.


#### Raises:

* <b>`ValueError`</b>: If none of the TPUs specified exists.



