description: Cluster Resolver for Google Cloud TPUs.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.cluster_resolver.TPUClusterResolver" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__enter__"/>
<meta itemprop="property" content="__exit__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="cluster_spec"/>
<meta itemprop="property" content="get_job_name"/>
<meta itemprop="property" content="get_master"/>
<meta itemprop="property" content="master"/>
<meta itemprop="property" content="num_accelerators"/>
</div>

# tf.distribute.cluster_resolver.TPUClusterResolver

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cluster_resolver/tpu_cluster_resolver.py#L51-L324">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Cluster Resolver for Google Cloud TPUs.

Inherits From: [`ClusterResolver`](../../../tf/distribute/cluster_resolver/ClusterResolver.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.cluster_resolver.TPUClusterResolver`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.cluster_resolver.TPUClusterResolver(
    tpu=None, zone=None, project=None, job_name='worker', coordinator_name=None,
    coordinator_address=None, credentials='default', service=None,
    discovery_url=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is an implementation of cluster resolvers for the Google Cloud TPU
service. As Cloud TPUs are in alpha, you will need to specify a API definition
file for this to consume, in addition to a list of Cloud TPUs in your Google
Cloud Platform project.

TPUClusterResolver supports the following distinct environments:
Google Compute Engine
Google Kubernetes Engine
Google internal

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tpu`
</td>
<td>
A string corresponding to the TPU to use. If the string is an empty
string, the string 'local', or a string that begins with 'grpc://', then
it is assumed to not correspond with a Cloud TPU and will instead be
passed as the session master and no ClusterSpec propagation will be
done. In the future, this may also support a list of strings when
multiple Cloud TPUs are used.
</td>
</tr><tr>
<td>
`zone`
</td>
<td>
Zone where the TPUs are located. If omitted or empty, we will assume
that the zone of the TPU is the same as the zone of the GCE VM, which we
will try to discover from the GCE metadata service.
</td>
</tr><tr>
<td>
`project`
</td>
<td>
Name of the GCP project containing Cloud TPUs. If omitted or
empty, we will try to discover the project name of the GCE VM from the
GCE metadata service.
</td>
</tr><tr>
<td>
`job_name`
</td>
<td>
Name of the TensorFlow job the TPUs belong to.
</td>
</tr><tr>
<td>
`coordinator_name`
</td>
<td>
The name to use for the coordinator. Set to None if the
coordinator should not be included in the computed ClusterSpec.
</td>
</tr><tr>
<td>
`coordinator_address`
</td>
<td>
The address of the coordinator (typically an ip:port
pair). If set to None, a TF server will be started. If coordinator_name
is None, a TF server will not be started even if coordinator_address is
None.
</td>
</tr><tr>
<td>
`credentials`
</td>
<td>
GCE Credentials. If None, then we use default credentials
from the oauth2client
</td>
</tr><tr>
<td>
`service`
</td>
<td>
The GCE API object returned by the googleapiclient.discovery
function. If you specify a custom service object, then the credentials
parameter will be ignored.
</td>
</tr><tr>
<td>
`discovery_url`
</td>
<td>
A URL template that points to the location of the discovery
service. It should have two parameters {api} and {apiVersion} that when
filled in produce an absolute URL to the discovery document for that
service. The environment variable 'TPU_API_DISCOVERY_URL' will override
this.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ImportError`
</td>
<td>
If the googleapiclient is not installed.
</td>
</tr><tr>
<td>
`ValueError`
</td>
<td>
If no TPUs are specified.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If an empty TPU name is specified and this is running in a
Google Cloud environment.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`environment`
</td>
<td>
Returns the current environment which TensorFlow is running in.
</td>
</tr>
</table>



## Methods

<h3 id="cluster_spec"><code>cluster_spec</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cluster_resolver/tpu_cluster_resolver.py#L222-L256">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>cluster_spec()
</code></pre>

Returns a ClusterSpec object based on the latest TPU information.

We retrieve the information from the GCE APIs every time this method is
called.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A ClusterSpec containing host information returned from Cloud TPUs,
or None.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
If the provided TPU is not healthy.
</td>
</tr>
</table>



<h3 id="get_job_name"><code>get_job_name</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cluster_resolver/tpu_cluster_resolver.py#L219-L220">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_job_name()
</code></pre>




<h3 id="get_master"><code>get_master</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cluster_resolver/tpu_cluster_resolver.py#L216-L217">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>get_master()
</code></pre>




<h3 id="master"><code>master</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cluster_resolver/tpu_cluster_resolver.py#L175-L214">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>master(
    task_type=None, task_id=None, rpc_layer=None
)
</code></pre>

Get the Master string to be used for the session.

In the normal case, this returns the grpc path (grpc://1.2.3.4:8470) of
first instance in the ClusterSpec returned by the cluster_spec function.

If a non-TPU name is used when constructing a TPUClusterResolver, that will
be returned instead (e.g. If the tpus argument's value when constructing
this TPUClusterResolver was 'grpc://10.240.1.2:8470',
'grpc://10.240.1.2:8470' will be returned).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`task_type`
</td>
<td>
(Optional, string) The type of the TensorFlow task of the
master.
</td>
</tr><tr>
<td>
`task_id`
</td>
<td>
(Optional, integer) The index of the TensorFlow task of the
master.
</td>
</tr><tr>
<td>
`rpc_layer`
</td>
<td>
(Optional, string) The RPC protocol TensorFlow should use to
communicate with TPUs.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
string, the connection string to use when creating a session.
</td>
</tr>

</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
If none of the TPUs specified exists.
</td>
</tr>
</table>



<h3 id="num_accelerators"><code>num_accelerators</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cluster_resolver/tpu_cluster_resolver.py#L258-L300">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>num_accelerators(
    task_type=None, task_id=None, config_proto=None
)
</code></pre>

Returns the number of TPU cores per worker.

Connects to the master and list all the devices present in the master,
and counts them up. Also verifies that the device counts per host in the
cluster is the same before returning the number of TPU cores per host.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`task_type`
</td>
<td>
Unused.
</td>
</tr><tr>
<td>
`task_id`
</td>
<td>
Unused.
</td>
</tr><tr>
<td>
`config_proto`
</td>
<td>
Used to create a connection to a TPU master in order to
retrieve the system metadata.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`RuntimeError`
</td>
<td>
If we cannot talk to a TPU worker after retrying or if the
number of TPU devices per host is different.
</td>
</tr>
</table>



<h3 id="__enter__"><code>__enter__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cluster_resolver/tpu_cluster_resolver.py#L169-L170">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__enter__()
</code></pre>




<h3 id="__exit__"><code>__exit__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cluster_resolver/tpu_cluster_resolver.py#L172-L173">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__exit__(
    type, value, traceback
)
</code></pre>






