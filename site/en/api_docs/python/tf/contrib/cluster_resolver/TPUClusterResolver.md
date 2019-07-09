page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.cluster_resolver.TPUClusterResolver

## Class `TPUClusterResolver`

Inherits From: [`ClusterResolver`](../../../tf/contrib/cluster_resolver/ClusterResolver)

### Aliases:

* Class `tf.contrib.cluster_resolver.TPUClusterResolver`
* Class `tf.contrib.cluster_resolver.python.training.TPUClusterResolver`
* Class `tf.contrib.cluster_resolver.python.training.tpu_cluster_resolver.TPUClusterResolver`



Defined in [`tensorflow/python/distribute/cluster_resolver/tpu_cluster_resolver.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/distribute/cluster_resolver/tpu_cluster_resolver.py).

Cluster Resolver for Google Cloud TPUs.

This is an implementation of cluster resolvers for the Google Cloud TPU
service. As Cloud TPUs are in alpha, you will need to specify a API definition
file for this to consume, in addition to a list of Cloud TPUs in your Google
Cloud Platform project.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    tpu=None,
    zone=None,
    project=None,
    job_name='worker',
    coordinator_name=None,
    coordinator_address=None,
    credentials='default',
    service=None,
    discovery_url=None
)
```

Creates a new TPUClusterResolver object.

The ClusterResolver will then use the parameters to query the Cloud TPU APIs
for the IP addresses and ports of each Cloud TPU listed.

#### Args:

* <b>`tpu`</b>: Either a string, or a list of strings corresponding to the TPUs to
    use. If the single string is the empty string, the string 'local', or a
    string that begins with 'grpc://' or '/bns', then it is assumed to not
    correspond with a Cloud TPU and will instead be passed as the session
    master and no ClusterSpec propagation will be done.
* <b>`zone`</b>: Zone where the TPUs are located. If omitted or empty, we will assume
    that the zone of the TPU is the same as the zone of the GCE VM, which we
    will try to discover from the GCE metadata service.
* <b>`project`</b>: Name of the GCP project containing Cloud TPUs. If omitted or
    empty, we will try to discover the project name of the GCE VM from the
    GCE metadata service.
* <b>`job_name`</b>: Name of the TensorFlow job the TPUs belong to.
* <b>`coordinator_name`</b>: The name to use for the coordinator. Set to None if the
    coordinator should not be included in the computed ClusterSpec.
* <b>`coordinator_address`</b>: The address of the coordinator (typically an ip:port
    pair). If set to None, a TF server will be started. If coordinator_name
    is None, a TF server will not be started even if coordinator_address is
    None.
* <b>`credentials`</b>: GCE Credentials. If None, then we use default credentials
    from the oauth2client
* <b>`service`</b>: The GCE API object returned by the googleapiclient.discovery
    function. If you specify a custom service object, then the credentials
    parameter will be ignored.
* <b>`discovery_url`</b>: A URL template that points to the location of
    the discovery service. It should have two parameters {api} and
    {apiVersion} that when filled in produce an absolute URL to the
    discovery document for that service. The environment variable
    'TPU_API_DISCOVERY_URL' will override this.


#### Raises:

* <b>`ImportError`</b>: If the googleapiclient is not installed.
* <b>`ValueError`</b>: If no TPUs are specified.



## Properties

<h3 id="environment"><code>environment</code></h3>

Returns the current environment which TensorFlow is running in.



## Methods

<h3 id="__deepcopy__"><code>__deepcopy__</code></h3>

``` python
__deepcopy__(memo)
```



<h3 id="cluster_spec"><code>cluster_spec</code></h3>

``` python
cluster_spec()
```

Returns a ClusterSpec object based on the latest TPU information.

We retrieve the information from the GCE APIs every time this method is
called.

#### Returns:

A ClusterSpec containing host information returned from Cloud TPUs.


#### Raises:

* <b>`RuntimeError`</b>: If the provided TPU is not healthy.

<h3 id="get_job_name"><code>get_job_name</code></h3>

``` python
get_job_name()
```



<h3 id="get_master"><code>get_master</code></h3>

``` python
get_master()
```



<h3 id="master"><code>master</code></h3>

``` python
master(
    task_type=None,
    task_index=None,
    rpc_layer=None
)
```

Get the Master string to be used for the session.

In the normal case, this returns the grpc path (grpc://1.2.3.4:8470) of
first instance in the ClusterSpec returned by the cluster_spec function.

If a non-TPU name is used when constructing a TPUClusterResolver, that will
be returned instead (e.g. If the tpus argument's value when constructing
this TPUClusterResolver was 'grpc://10.240.1.2:8470',
'grpc://10.240.1.2:8470' will be returned).

#### Args:

* <b>`task_type`</b>: (Optional, string) The type of the TensorFlow task of the
    master.
* <b>`task_index`</b>: (Optional, integer) The index of the TensorFlow task of the
    master.
* <b>`rpc_layer`</b>: (Optional, string) The RPC protocol TensorFlow should use to
    communicate with TPUs.


#### Returns:

string, the connection string to use when creating a session.


#### Raises:

* <b>`ValueError`</b>: If none of the TPUs specified exists.

<h3 id="num_accelerators"><code>num_accelerators</code></h3>

``` python
num_accelerators(
    task_type=None,
    task_index=None,
    accelerator_type='TPU',
    config_proto=None
)
```

Returns the number of TPU cores per worker.

Connects to the master and list all the devices present in the master,
and counts them up. Also verifies that the device counts per host in the
cluster is the same before returning the number of TPU cores per host.

#### Args:

* <b>`task_type`</b>: Unused.
* <b>`task_index`</b>: Unused.
* <b>`accelerator_type`</b>: Unused.
* <b>`config_proto`</b>: Used to create a connection to a TPU master in order to
    retrieve the system metadata.


#### Raises:

* <b>`RuntimeError`</b>: If we cannot talk to a TPU worker after retrying or if the
    number of TPU devices per host is different.



