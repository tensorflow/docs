description: Abstract class for all implementations of ClusterResolvers.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.distribute.cluster_resolver.ClusterResolver" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="cluster_spec"/>
<meta itemprop="property" content="master"/>
<meta itemprop="property" content="num_accelerators"/>
</div>

# tf.distribute.cluster_resolver.ClusterResolver

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L61-L289">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



Abstract class for all implementations of ClusterResolvers.

<section class="expandable">
  <h4 class="showalways">View aliases</h4>
  <p>
<b>Compat aliases for migration</b>
<p>See
<a href="https://www.tensorflow.org/guide/migrate">Migration guide</a> for
more details.</p>
<p>`tf.compat.v1.distribute.cluster_resolver.ClusterResolver`</p>
</p>
</section>

<!-- Placeholder for "Used in" -->

This defines the skeleton for all implementations of ClusterResolvers.
ClusterResolvers are a way for TensorFlow to communicate with various cluster
management systems (e.g. GCE, AWS, etc...) and gives TensorFlow necessary
information to set up distributed training.

By letting TensorFlow communicate with these systems, we will be able to
automatically discover and resolve IP addresses for various TensorFlow
workers. This will eventually allow us to automatically recover from
underlying machine failures and scale TensorFlow worker clusters up and down.

Note to Implementors of <a href="../../../tf/distribute/cluster_resolver/ClusterResolver.md"><code>tf.distribute.cluster_resolver.ClusterResolver</code></a>
subclass: In addition to these abstract methods, when task_type, task_id, and
rpc_layer attributes are applicable, you should also implement them either as
properties with getters or setters, or directly set the attributes
`self._task_type`, `self._task_id`, or `self._rpc_layer` so the base class'
getters and setters are used. See
<a href="../../../tf/distribute/cluster_resolver/SimpleClusterResolver.md#__init__"><code>tf.distribute.cluster_resolver.SimpleClusterResolver.__init__</code></a> for an
example.

In general, multi-client tf.distribute strategies such as
<a href="../../../tf/distribute/experimental/MultiWorkerMirroredStrategy.md"><code>tf.distribute.experimental.MultiWorkerMirroredStrategy</code></a> require task_type and
task_id properties to be available in the `ClusterResolver` they are using. On
the other hand, these concepts are not applicable in single-client strategies,
such as <a href="../../../tf/distribute/experimental/TPUStrategy.md"><code>tf.distribute.experimental.TPUStrategy</code></a>, because the program is only
expected to be run on one task, so there should not be a need to have code
branches according to task type and task id.

- task_type is the name of the server's current named job (e.g. 'worker',
   'ps' in a distributed parameterized training job).
- task_id is the ordinal index of the server within the task type.
- rpc_layer is the protocol used by TensorFlow to communicate with other
    TensorFlow servers in a distributed environment.



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

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L98-L112">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>cluster_spec()
</code></pre>

Retrieve the current state of the cluster and return a <a href="../../../tf/train/ClusterSpec.md"><code>tf.train.ClusterSpec</code></a>.


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
A <a href="../../../tf/train/ClusterSpec.md"><code>tf.train.ClusterSpec</code></a> representing the state of the cluster at the
moment this function is called.
</td>
</tr>

</table>


Implementors of this function must take care in ensuring that the
ClusterSpec returned is up-to-date at the time of calling this function.
This usually means retrieving the information from the underlying cluster
management system every time this function is invoked and reconstructing
a cluster_spec, rather than attempting to cache anything.

<h3 id="master"><code>master</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L114-L132">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>@abc.abstractmethod</code>
<code>master(
    task_type=None, task_id=None, rpc_layer=None
)
</code></pre>

Retrieves the name or URL of the session master.

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


Implementors of this function must take care in ensuring that the master
returned is up-to-date at the time to calling this function. This usually
means retrieving the master every time this function is invoked.

<h3 id="num_accelerators"><code>num_accelerators</code></h3>

<a target="_blank" href="https://github.com/tensorflow/tensorflow/blob/r2.4/tensorflow/python/distribute/cluster_resolver/cluster_resolver.py#L134-L171">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>num_accelerators(
    task_type=None, task_id=None, config_proto=None
)
</code></pre>

Returns the number of accelerator cores per worker.

This returns the number of accelerator cores (such as GPUs and TPUs)
available per worker.

Optionally, we allow callers to specify the task_type, and task_id, for
if they want to target a specific TensorFlow task to query
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





