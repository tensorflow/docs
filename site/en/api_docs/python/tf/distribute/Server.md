description: An in-process TensorFlow server, for use in distributed training.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.Server" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="create_local_server"/>
<meta itemprop="property" content="join"/>
<meta itemprop="property" content="start"/>
</div>

# tf.distribute.Server

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/server_lib.py#L100-L243">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



An in-process TensorFlow server, for use in distributed training.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.Server`, `tf.compat.v1.train.Server`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.Server(
    server_or_cluster_def, job_name=None, task_index=None, protocol=None,
    config=None, start=(True)
)
</code></pre>



<!-- Placeholder for "Used in" -->

A <a href="../../tf/distribute/Server.md"><code>tf.distribute.Server</code></a> instance encapsulates a set of devices and a
<a href="../../tf/compat/v1/Session.md"><code>tf.compat.v1.Session</code></a> target that
can participate in distributed training. A server belongs to a
cluster (specified by a <a href="../../tf/train/ClusterSpec.md"><code>tf.train.ClusterSpec</code></a>), and
corresponds to a particular task in a named job. The server can
communicate with any other server in the same cluster.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`server_or_cluster_def`
</td>
<td>
A <a href="../../tf/train/ServerDef.md"><code>tf.train.ServerDef</code></a> or <a href="../../tf/train/ClusterDef.md"><code>tf.train.ClusterDef</code></a>
protocol buffer, or a <a href="../../tf/train/ClusterSpec.md"><code>tf.train.ClusterSpec</code></a> object, describing the
server to be created and/or the cluster of which it is a member.
</td>
</tr><tr>
<td>
`job_name`
</td>
<td>
(Optional.) Specifies the name of the job of which the server is
a member. Defaults to the value in `server_or_cluster_def`, if
specified.
</td>
</tr><tr>
<td>
`task_index`
</td>
<td>
(Optional.) Specifies the task index of the server in its job.
Defaults to the value in `server_or_cluster_def`, if specified.
Otherwise defaults to 0 if the server's job has only one task.
</td>
</tr><tr>
<td>
`protocol`
</td>
<td>
(Optional.) Specifies the protocol to be used by the server.
Acceptable values include `"grpc", "grpc+verbs"`. Defaults to the value
in `server_or_cluster_def`, if specified. Otherwise defaults to
`"grpc"`.
</td>
</tr><tr>
<td>
`config`
</td>
<td>
(Options.) A <a href="../../tf/compat/v1/ConfigProto.md"><code>tf.compat.v1.ConfigProto</code></a> that specifies default
configuration options for all sessions that run on this server.
</td>
</tr><tr>
<td>
`start`
</td>
<td>
(Optional.) Boolean, indicating whether to start the server after
creating it. Defaults to `True`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`tf.errors.OpError`
</td>
<td>
Or one of its subclasses if an error occurs while
creating the TensorFlow server.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`server_def`
</td>
<td>
Returns the <a href="../../tf/train/ServerDef.md"><code>tf.train.ServerDef</code></a> for this server.
</td>
</tr><tr>
<td>
`target`
</td>
<td>
Returns the target for a <a href="../../tf/compat/v1/Session.md"><code>tf.compat.v1.Session</code></a> to connect to this server.

To create a
<a href="../../tf/compat/v1/Session.md"><code>tf.compat.v1.Session</code></a> that
connects to this server, use the following snippet:

```python
server = tf.distribute.Server(...)
with tf.compat.v1.Session(server.target):
# ...
```
</td>
</tr>
</table>



## Methods

<h3 id="create_local_server"><code>create_local_server</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/server_lib.py#L220-L243">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@staticmethod</code>
<code>create_local_server(
    config=None, start=(True)
)
</code></pre>

Creates a new single-process cluster running on the local host.

This method is a convenience wrapper for creating a
<a href="../../tf/distribute/Server.md"><code>tf.distribute.Server</code></a> with a <a href="../../tf/train/ServerDef.md"><code>tf.train.ServerDef</code></a> that specifies a
single-process cluster containing a single task in a job called
`"local"`.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`config`
</td>
<td>
(Options.) A <a href="../../tf/compat/v1/ConfigProto.md"><code>tf.compat.v1.ConfigProto</code></a> that specifies default
configuration options for all sessions that run on this server.
</td>
</tr><tr>
<td>
`start`
</td>
<td>
(Optional.) Boolean, indicating whether to start the server after
creating it. Defaults to `True`.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A local <a href="../../tf/distribute/Server.md"><code>tf.distribute.Server</code></a>.
</td>
</tr>

</table>



<h3 id="join"><code>join</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/server_lib.py#L180-L189">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>join()
</code></pre>

Blocks until the server has shut down.

This method currently blocks forever.

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`tf.errors.OpError`
</td>
<td>
Or one of its subclasses if an error occurs while
joining the TensorFlow server.
</td>
</tr>
</table>



<h3 id="start"><code>start</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/training/server_lib.py#L171-L178">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>start()
</code></pre>

Starts this server.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Raises</th></tr>

<tr>
<td>
`tf.errors.OpError`
</td>
<td>
Or one of its subclasses if an error occurs while
starting the TensorFlow server.
</td>
</tr>
</table>





