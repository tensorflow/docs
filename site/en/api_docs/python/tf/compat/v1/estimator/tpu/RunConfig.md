description: RunConfig with TPU support.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.estimator.tpu.RunConfig" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__init__"/>
<meta itemprop="property" content="replace"/>
</div>

# tf.compat.v1.estimator.tpu.RunConfig

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/tpu_config.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



RunConfig with TPU support.

Inherits From: [`RunConfig`](../../../../../tf/estimator/RunConfig.md)

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.estimator.tpu.RunConfig(
    tpu_config=None, evaluation_master=None, master=None, cluster=None, **kwargs
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`tpu_config`
</td>
<td>
the TPUConfig that specifies TPU-specific configuration.
</td>
</tr><tr>
<td>
`evaluation_master`
</td>
<td>
a string. The address of the master to use for eval.
Defaults to master if not set.
</td>
</tr><tr>
<td>
`master`
</td>
<td>
a string. The address of the master to use for training.
</td>
</tr><tr>
<td>
`cluster`
</td>
<td>
a ClusterResolver
</td>
</tr><tr>
<td>
`**kwargs`
</td>
<td>
keyword config parameters.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Raises</h2></th></tr>

<tr>
<td>
`ValueError`
</td>
<td>
if cluster is not None and the provided session_config has a
cluster_def already.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`checkpoint_save_graph_def`
</td>
<td>

</td>
</tr><tr>
<td>
`cluster`
</td>
<td>

</td>
</tr><tr>
<td>
`cluster_spec`
</td>
<td>

</td>
</tr><tr>
<td>
`device_fn`
</td>
<td>
Returns the device_fn.

If device_fn is not `None`, it overrides the default
device function used in `Estimator`.
Otherwise the default one is used.
</td>
</tr><tr>
<td>
`eval_distribute`
</td>
<td>
Optional <a href="../../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> for evaluation.
</td>
</tr><tr>
<td>
`evaluation_master`
</td>
<td>

</td>
</tr><tr>
<td>
`experimental_max_worker_delay_secs`
</td>
<td>

</td>
</tr><tr>
<td>
`global_id_in_cluster`
</td>
<td>
The global id in the training cluster.

All global ids in the training cluster are assigned from an increasing
sequence of consecutive integers. The first id is 0.

Note: Task id (the property field `task_id`) is tracking the index of the
node among all nodes with the SAME task type. For example, given the cluster
definition as follows:

```
cluster = {'chief': ['host0:2222'],
'ps': ['host1:2222', 'host2:2222'],
'worker': ['host3:2222', 'host4:2222', 'host5:2222']}
```

Nodes with task type `worker` can have id 0, 1, 2.  Nodes with task type
`ps` can have id, 0, 1. So, `task_id` is not unique, but the pair
(`task_type`, `task_id`) can uniquely determine a node in the cluster.

Global id, i.e., this field, is tracking the index of the node among ALL
nodes in the cluster. It is uniquely assigned.  For example, for the cluster
spec given above, the global ids are assigned as:
```
task_type  | task_id  |  global_id
--------------------------------
chief      | 0        |  0
worker     | 0        |  1
worker     | 1        |  2
worker     | 2        |  3
ps         | 0        |  4
ps         | 1        |  5
```
</td>
</tr><tr>
<td>
`is_chief`
</td>
<td>

</td>
</tr><tr>
<td>
`keep_checkpoint_every_n_hours`
</td>
<td>

</td>
</tr><tr>
<td>
`keep_checkpoint_max`
</td>
<td>

</td>
</tr><tr>
<td>
`log_step_count_steps`
</td>
<td>

</td>
</tr><tr>
<td>
`master`
</td>
<td>

</td>
</tr><tr>
<td>
`model_dir`
</td>
<td>

</td>
</tr><tr>
<td>
`num_ps_replicas`
</td>
<td>

</td>
</tr><tr>
<td>
`num_worker_replicas`
</td>
<td>

</td>
</tr><tr>
<td>
`protocol`
</td>
<td>
Returns the optional protocol value.
</td>
</tr><tr>
<td>
`save_checkpoints_secs`
</td>
<td>

</td>
</tr><tr>
<td>
`save_checkpoints_steps`
</td>
<td>

</td>
</tr><tr>
<td>
`save_summary_steps`
</td>
<td>

</td>
</tr><tr>
<td>
`service`
</td>
<td>
Returns the platform defined (in TF_CONFIG) service dict.
</td>
</tr><tr>
<td>
`session_config`
</td>
<td>

</td>
</tr><tr>
<td>
`session_creation_timeout_secs`
</td>
<td>

</td>
</tr><tr>
<td>
`task_id`
</td>
<td>

</td>
</tr><tr>
<td>
`task_type`
</td>
<td>

</td>
</tr><tr>
<td>
`tf_random_seed`
</td>
<td>

</td>
</tr><tr>
<td>
`tpu_config`
</td>
<td>

</td>
</tr><tr>
<td>
`train_distribute`
</td>
<td>
Optional <a href="../../../../../tf/distribute/Strategy.md"><code>tf.distribute.Strategy</code></a> for training.
</td>
</tr>
</table>



## Methods

<h3 id="replace"><code>replace</code></h3>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/tpu_config.py">View source</a>

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>replace(
    **kwargs
)
</code></pre>

Returns a new instance of `RunConfig` replacing specified properties.

Only the properties in the following list are allowed to be replaced:

  - `model_dir`,
  - `tf_random_seed`,
  - `save_summary_steps`,
  - `save_checkpoints_steps`,
  - `save_checkpoints_secs`,
  - `session_config`,
  - `keep_checkpoint_max`,
  - `keep_checkpoint_every_n_hours`,
  - `log_step_count_steps`,
  - `train_distribute`,
  - `device_fn`,
  - `protocol`.
  - `eval_distribute`,
  - `experimental_distribute`,
  - `experimental_max_worker_delay_secs`,

In addition, either `save_checkpoints_steps` or `save_checkpoints_secs`
can be set (should not be both).

<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Args</th></tr>

<tr>
<td>
`**kwargs`
</td>
<td>
keyword named properties with new values.
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
If any property name in `kwargs` does not exist or is not
allowed to be replaced, or both `save_checkpoints_steps` and
`save_checkpoints_secs` are set.
</td>
</tr>
</table>



<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2">Returns</th></tr>
<tr class="alt">
<td colspan="2">
a new instance of `RunConfig`.
</td>
</tr>

</table>





