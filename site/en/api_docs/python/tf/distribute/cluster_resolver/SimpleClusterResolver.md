description: Simple implementation of ClusterResolver that accepts all attributes.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.cluster_resolver.SimpleClusterResolver" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="cluster_spec"/>
<meta itemprop="property" content="master"/>
<meta itemprop="property" content="num_accelerators"/>
</div>

# tf.distribute.cluster_resolver.SimpleClusterResolver

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L293-L419">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Simple implementation of ClusterResolver that accepts all attributes.

Inherits From: [`ClusterResolver`](../../../tf/distribute/cluster_resolver/ClusterResolver.md)

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.cluster_resolver.SimpleClusterResolver`</p>
</p>
</section>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.distribute.cluster_resolver.SimpleClusterResolver(
    cluster_spec, master='', task_type=None, task_id=None, environment='',
    num_accelerators=None, rpc_layer=None
)
</code></pre>



<!-- Placeholder for "Used in" -->

Please see the base class for documentation of arguments of its constructor.

It is useful if you want to specify some or all attributes.

Usage example with <a href="../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a>:

  ```Python
  cluster = tf.train.ClusterSpec({"worker": ["worker0.example.com:2222",
                                             "worker1.example.com:2222"]})

  # On worker 0
  cluster_resolver = SimpleClusterResolver(cluster, task_type="worker",
                                           task_id=0,
                                           num_accelerators={"GPU": 8},
                                           rpc_layer="grpc")
  strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(
      cluster_resolver=cluster_resolver)

  # On worker 1
  cluster_resolver = SimpleClusterResolver(cluster, task_type="worker",
                                           task_id=1,
                                           num_accelerators={"GPU": 8},
                                           rpc_layer="grpc")
  strategy = tf.distribute.experimental.MultiWorkerMirroredStrategy(
      cluster_resolver=cluster_resolver)
  ```



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
</tr><tr>
<td>
`rpc_layer`
</td>
<td>

</td>
</tr><tr>
<td>
`task_id`
</td>
<td>
Returns the task id this `ClusterResolver` indicates.

In TensorFlow distributed environment, each job may have an applicable
task id, which is the index of the instance within its task type. This is
useful when user needs to run specific code according to task index. For
example,

```python
cluster_spec = tf.train.ClusterSpec({
"ps": ["localhost:2222", "localhost:2223"],
"worker": ["localhost:2224", "localhost:2225", "localhost:2226"]
})

# SimpleClusterResolver is used here for illustration; other cluster
# resolvers may be used for other source of task type/id.
simple_resolver = SimpleClusterResolver(cluster_spec, task_type="worker",
task_id=0)

...

if cluster_resolver.task_type == 'worker' and cluster_resolver.task_id == 0:
# Perform something that's only applicable on 'worker' type, id 0. This
# block will run on this particular instance since we've specified this
# task to be a 'worker', id 0 in above cluster resolver.
else:
# Perform something that's only applicable on other ids. This block will
# not run on this particular instance.
```

Returns `None` if such information is not available or is not applicable
in the current distributed environment, such as training with
<a href="../../../tf/distribute/cluster_resolver/TPUClusterResolver.md"><code>tf.distribute.cluster_resolver.TPUClusterResolver</code></a>.

For more information, please see
<a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a>'s class docstring.
</td>
</tr><tr>
<td>
`task_type`
</td>
<td>
Returns the task type this `ClusterResolver` indicates.

In TensorFlow distributed environment, each job may have an applicable
task type. Valid task types in TensorFlow include
'chief': a worker that is designated with more responsibility,
'worker': a regular worker for training/evaluation,
'ps': a parameter server, or
'evaluator': an evaluator that evaluates the checkpoints for metrics.

See [Multi-worker configuration](
https://www.tensorflow.org/tutorials/distribute/multi_worker_with_keras#multi-worker_configuration)
for more information about 'chief' and 'worker' task type, which are most
commonly used.

Having access to such information is useful when user needs to run specific
code according to task types. For example,

```python
cluster_spec = tf.train.ClusterSpec({
"ps": ["localhost:2222", "localhost:2223"],
"worker": ["localhost:2224", "localhost:2225", "localhost:2226"]
})

# SimpleClusterResolver is used here for illustration; other cluster
# resolvers may be used for other source of task type/id.
simple_resolver = SimpleClusterResolver(cluster_spec, task_type="worker",
task_id=1)

...

if cluster_resolver.task_type == 'worker':
# Perform something that's only applicable on workers. This block
# will run on this particular instance since we've specified this task to
# be a worker in above cluster resolver.
elif cluster_resolver.task_type == 'ps':
# Perform something that's only applicable on parameter servers. This
# block will not run on this particular instance.
```

Returns `None` if such information is not available or is not applicable
in the current distributed environment, such as training with
<a href="../../../tf/distribute/experimental/TPUStrategy.md"><code>tf.distribute.experimental.TPUStrategy</code></a>.

For more information, please see
<a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a>'s class doc.
</td>
</tr>
</table>



## Methods

<h3 id="cluster_spec"><code>cluster_spec</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L345-L347">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>cluster_spec()
</code></pre>

Returns the ClusterSpec passed into the constructor.


<h3 id="master"><code>master</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L349-L370">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>master(
    task_type=None, task_id=None, rpc_layer=None
)
</code></pre>

Returns the master address to use when creating a session.

Note: this is only useful for TensorFlow 1.x.

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
(Optional) The RPC used by distributed TensorFlow.
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


If a task_type and task_id is given, this will override the `master`
string passed into the initialization function.

<h3 id="num_accelerators"><code>num_accelerators</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.3/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L392-L411">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>num_accelerators(
    task_type=None, task_id=None, config_proto=None
)
</code></pre>

Returns the number of accelerator cores per worker.

The SimpleClusterResolver does not do automatic detection of accelerators,
and thus all arguments are unused and we simply return the value provided
in the constructor.

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
Unused.
</td>
</tr>
</table>





