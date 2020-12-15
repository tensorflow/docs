description: Create and start local servers and return the associated Server objects.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.test.create_local_cluster" />
<meta itemprop="path" content="Stable" />
</div>

# tf.test.create_local_cluster

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/framework/test_util.py#L3163-L3249">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Create and start local servers and return the associated `Server` objects.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.test.create_local_cluster`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.test.create_local_cluster(
    num_workers, num_ps, protocol='grpc', worker_config=None, ps_config=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

"PS" stands for "parameter server": a task responsible for storing and
updating the model's parameters. Other tasks send updates to these parameters
as they work on optimizing the parameters. This particular division of labor
between tasks is not required, but is common for distributed training.

Read more at https://www.tensorflow.org/guide/extend/architecture

![components](https://www.tensorflow.org/images/diag1.svg "components")


Figure illustrates the interaction of these components.
"/job:worker/task:0" and "/job:ps/task:0" are both tasks with worker services.


#### Example:


```python
workers, _ = tf.test.create_local_cluster(num_workers=2, num_ps=2)

worker_sessions = [tf.compat.v1.Session(w.target) for w in workers]

with tf.device("/job:ps/task:0"):
  ...
with tf.device("/job:ps/task:1"):
  ...
with tf.device("/job:worker/task:0"):
  ...
with tf.device("/job:worker/task:1"):
  ...

worker_sessions[0].run(...)
```

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`num_workers`
</td>
<td>
Number of worker servers to start.
</td>
</tr><tr>
<td>
`num_ps`
</td>
<td>
Number of PS servers to start.
</td>
</tr><tr>
<td>
`protocol`
</td>
<td>
Communication protocol. Allowed values are documented in the
documentation of <a href="../../tf/distribute/Server.md"><code>tf.distribute.Server</code></a>.
</td>
</tr><tr>
<td>
`worker_config`
</td>
<td>
(optional) `tf.ConfigProto` to initialize workers. Can be
used to instantiate multiple devices etc.
</td>
</tr><tr>
<td>
`ps_config`
</td>
<td>
(optional) `tf.ConfigProto` to initialize PS servers.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Returns</h2></th></tr>
<tr class="alt">
<td colspan="2">
A tuple `(worker_servers, ps_servers)`.  `worker_servers` is a list
of `num_workers` objects of type <a href="../../tf/distribute/Server.md"><code>tf.distribute.Server</code></a> (all running
locally);
and `ps_servers` is a list of `num_ps` objects of similar type.
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
if portpicker module was not found at load time
</td>
</tr>
</table>

