description: Represents a cluster as a set of "tasks", organized into "jobs".

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.train.ClusterSpec" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__bool__"/>
<meta itemprop="property" content="__eq__"/>
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="__ne__"/>
<meta itemprop="property" content="__nonzero__"/>
<meta itemprop="property" content="as_cluster_def"/>
<meta itemprop="property" content="as_dict"/>
<meta itemprop="property" content="job_tasks"/>
<meta itemprop="property" content="num_tasks"/>
<meta itemprop="property" content="task_address"/>
<meta itemprop="property" content="task_indices"/>
</div>

# tf.train.ClusterSpec

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/server_lib.py#L242-L491">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Represents a cluster as a set of "tasks", organized into "jobs".

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.train.ClusterSpec`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.train.ClusterSpec(
    cluster
)
</code></pre>



<!-- Placeholder for "Used in" -->

A <a href="../../tf/train/ClusterSpec.md"><code>tf.train.ClusterSpec</code></a> represents the set of processes that
participate in a distributed TensorFlow computation. Every
<a href="../../tf/distribute/Server.md"><code>tf.distribute.Server</code></a> is constructed in a particular cluster.

To create a cluster with two jobs and five tasks, you specify the
mapping from job names to lists of network addresses (typically
hostname-port pairs).

```python
cluster = tf.train.ClusterSpec({"worker": ["worker0.example.com:2222",
                                           "worker1.example.com:2222",
                                           "worker2.example.com:2222"],
                                "ps": ["ps0.example.com:2222",
                                       "ps1.example.com:2222"]})
```

Each job may also be specified as a sparse mapping from task indices
to network addresses. This enables a server to be configured without
needing to know the identity of (for example) all other worker
tasks:

```python
cluster = tf.train.ClusterSpec({"worker": {1: "worker1.example.com:2222"},
                                "ps": ["ps0.example.com:2222",
                                       "ps1.example.com:2222"]})
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`cluster`
</td>
<td>
A dictionary mapping one or more job names to (i) a list of
network addresses, or (ii) a dictionary mapping integer task indices to
network addresses; or a <a href="../../tf/train/ClusterDef.md"><code>tf.train.ClusterDef</code></a> protocol buffer.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`TypeError`
</td>
<td>
If `cluster` is not a dictionary mapping strings to lists
of strings, and not a <a href="../../tf/train/ClusterDef.md"><code>tf.train.ClusterDef</code></a> protobuf.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`jobs`
</td>
<td>
Returns a list of job names in this cluster.
</td>
</tr>
</table>



## Methods

<h3 id="as_cluster_def"><code>as_cluster_def</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/server_lib.py#L363-L365">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>as_cluster_def()
</code></pre>

Returns a <a href="../../tf/train/ClusterDef.md"><code>tf.train.ClusterDef</code></a> protocol buffer based on this cluster.


<h3 id="as_dict"><code>as_dict</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/server_lib.py#L336-L361">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>as_dict()
</code></pre>

Returns a dictionary from job names to their tasks.

For each job, if the task index space is dense, the corresponding
value will be a list of network addresses; otherwise it will be a
dictionary mapping (sparse) task indices to the corresponding
addresses.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A dictionary mapping job names to lists or dictionaries
describing the tasks in those jobs.
</td>
</tr>

</table>



<h3 id="job_tasks"><code>job_tasks</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/server_lib.py#L437-L464">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>job_tasks(
    job_name
)
</code></pre>

Returns a mapping from task ID to address in the given job.

NOTE: For backwards compatibility, this method returns a list. If
the given job was defined with a sparse set of task indices, the
length of this list may not reflect the number of tasks defined in
this job. Use the <a href="../../tf/train/ClusterSpec.md#num_tasks"><code>tf.train.ClusterSpec.num_tasks</code></a> method
to find the number of tasks defined in a particular job.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`job_name`
</td>
<td>
The string name of a job in this cluster.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of task addresses, where the index in the list
corresponds to the task index of each task. The list may contain
`None` if the job was defined with a sparse set of task indices.
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
If `job_name` does not name a job in this cluster.
</td>
</tr>
</table>



<h3 id="num_tasks"><code>num_tasks</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/server_lib.py#L376-L392">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>num_tasks(
    job_name
)
</code></pre>

Returns the number of tasks defined in the given job.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`job_name`
</td>
<td>
The string name of a job in this cluster.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The number of tasks defined in the given job.
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
If `job_name` does not name a job in this cluster.
</td>
</tr>
</table>



<h3 id="task_address"><code>task_address</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/server_lib.py#L413-L435">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>task_address(
    job_name, task_index
)
</code></pre>

Returns the address of the given task in the given job.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`job_name`
</td>
<td>
The string name of a job in this cluster.
</td>
</tr><tr>
<td>
`task_index`
</td>
<td>
A non-negative integer.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
The address of the given task in the given job.
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
If `job_name` does not name a job in this cluster,
or no task with index `task_index` is defined in that job.
</td>
</tr>
</table>



<h3 id="task_indices"><code>task_indices</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/server_lib.py#L394-L411">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>task_indices(
    job_name
)
</code></pre>

Returns a list of valid task indices in the given job.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`job_name`
</td>
<td>
The string name of a job in this cluster.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A list of valid task indices in the given job.
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
If `job_name` does not name a job in this cluster,
or no task with index `task_index` is defined in that job.
</td>
</tr>
</table>



<h3 id="__bool__"><code>__bool__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/server_lib.py#L317-L318">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__bool__()
</code></pre>




<h3 id="__eq__"><code>__eq__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/server_lib.py#L323-L324">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__eq__(
    other
)
</code></pre>

Return self==value.


<h3 id="__ne__"><code>__ne__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/server_lib.py#L326-L327">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__ne__(
    other
)
</code></pre>

Return self!=value.


<h3 id="__nonzero__"><code>__nonzero__</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.2/tensorflow/python/training/server_lib.py#L317-L318">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>__nonzero__()
</code></pre>






