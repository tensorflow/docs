description: ClusterResolver for Kubernetes.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.cluster_resolver.KubernetesClusterResolver" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="cluster_spec"/>
<meta itemprop="property" content="master"/>
<meta itemprop="property" content="num_accelerators"/>
</div>

# tf.distribute.cluster_resolver.KubernetesClusterResolver

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver.py#L35-L158">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



ClusterResolver for Kubernetes.

Inherits From: [`ClusterResolver`](../../../tf/distribute/cluster_resolver/ClusterResolver.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.cluster_resolver.KubernetesClusterResolver`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.cluster_resolver.KubernetesClusterResolver(
    job_to_label_mapping=None, tf_server_port=8470, rpc_layer='grpc',
    override_client=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

This is an implementation of cluster resolvers for Kubernetes. When given the
the Kubernetes namespace and label selector for pods, we will retrieve the
pod IP addresses of all running pods matching the selector, and return a
ClusterSpec based on that information.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`job_to_label_mapping`
</td>
<td>
A mapping of TensorFlow jobs to label selectors.
This allows users to specify many TensorFlow jobs in one Cluster
Resolver, and each job can have pods belong with different label
selectors. For example, a sample mapping might be
```
{'worker': ['job-name=worker-cluster-a', 'job-name=worker-cluster-b'],
'ps': ['job-name=ps-1', 'job-name=ps-2']}
```
</td>
</tr><tr>
<td>
`tf_server_port`
</td>
<td>
The port the TensorFlow server is listening on.
</td>
</tr><tr>
<td>
`rpc_layer`
</td>
<td>
(Optional) The RPC layer TensorFlow should use to communicate
between tasks in Kubernetes. Defaults to 'grpc'.
</td>
</tr><tr>
<td>
`override_client`
</td>
<td>
The Kubernetes client (usually automatically retrieved
using `from kubernetes import client as k8sclient`). If you pass this
in, you are responsible for setting Kubernetes credentials manually.
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
If the Kubernetes Python client is not installed and no
`override_client` is passed in.
</td>
</tr><tr>
<td>
`RuntimeError`
</td>
<td>
If autoresolve_task is not a boolean or a callable.
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

There are two possible return values, "google" (when TensorFlow is running
in a Google-internal environment) or an empty string (when TensorFlow is
running elsewhere).

If you are implementing a ClusterResolver that works in both the Google
environment and the open-source world (for instance, a TPU ClusterResolver
or similar), you will have to return the appropriate string depending on the
environment, which you will have to detect.

Otherwise, if you are implementing a ClusterResolver that will only work
in open-source TensorFlow, you do not need to implement this property.
</td>
</tr>
</table>



## Methods

<h3 id="cluster_spec"><code>cluster_spec</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver.py#L122-L158">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>cluster_spec()
</code></pre>

Returns a ClusterSpec object based on the latest info from Kubernetes.

We retrieve the information from the Kubernetes master every time this
method is called.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A ClusterSpec containing host information returned from Kubernetes.
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
If any of the pods returned by the master is not in the
`Running` phase.
</td>
</tr>
</table>



<h3 id="master"><code>master</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cluster_resolver/kubernetes_cluster_resolver.py#L96-L120">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>master(
    task_type=None, task_id=None, rpc_layer=None
)
</code></pre>

Returns the master address to use when creating a session.

You must have set the task_type and task_id object properties before
calling this function, or pass in the `task_type` and `task_id`
parameters when using this function. If you do both, the function parameters
will override the object properties.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`task_type`
</td>
<td>
(Optional) The type of the TensorFlow task of the master.
</td>
</tr><tr>
<td>
`task_id`
</td>
<td>
(Optional) The index of the TensorFlow task of the master.
</td>
</tr><tr>
<td>
`rpc_layer`
</td>
<td>
(Optional) The RPC protocol for the given cluster.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The name or URL of the session master.
</td>
</tr>

</table>



<h3 id="num_accelerators"><code>num_accelerators</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L119-L154">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>num_accelerators(
    task_type=None, task_id=None, config_proto=None
)
</code></pre>

Returns the number of accelerator cores per worker.

This returns the number of accelerator cores (such as GPUs and TPUs)
available per worker.

Optionally, we allow callers to specify the task_type, and task_id, for
if they want to target a specific TensorFlow process to query
the number of accelerators. This is to support heterogenous environments,
where the number of accelerators cores per host is different.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`task_type`
</td>
<td>
(Optional) The type of the TensorFlow task of the machine we
want to query.
</td>
</tr><tr>
<td>
`task_id`
</td>
<td>
(Optional) The index of the TensorFlow task of the machine we
want to query.
</td>
</tr><tr>
<td>
`config_proto`
</td>
<td>
(Optional) Configuration for starting a new session to
query how many accelerator cores it has.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A map of accelerator types to number of cores.
</td>
</tr>

</table>





