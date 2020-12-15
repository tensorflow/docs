description: TPU related configuration required by TPUEstimator.

<div itemscope itemtype="http://developers.google.com/ReferenceObject">
<meta itemprop="name" content="tf.compat.v1.estimator.tpu.TPUConfig" />
<meta itemprop="path" content="Stable" />
<meta itemprop="property" content="__new__"/>
<meta itemprop="property" content="eval_training_input_configuration"/>
<meta itemprop="property" content="experimental_allow_per_host_v2_parallel_get_next"/>
<meta itemprop="property" content="experimental_feed_hook"/>
<meta itemprop="property" content="experimental_host_call_every_n_steps"/>
<meta itemprop="property" content="initial_infeed_sleep_secs"/>
<meta itemprop="property" content="input_partition_dims"/>
<meta itemprop="property" content="iterations_per_loop"/>
<meta itemprop="property" content="num_cores_per_replica"/>
<meta itemprop="property" content="num_shards"/>
<meta itemprop="property" content="per_host_input_for_training"/>
<meta itemprop="property" content="tpu_job_name"/>
</div>

# tf.compat.v1.estimator.tpu.TPUConfig

<!-- Insert buttons and diff -->

<table class="tfo-notebook-buttons tfo-api nocontent" align="left">
<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/tpu_config.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td>
</table>



TPU related configuration required by `TPUEstimator`.

<pre class="devsite-click-to-copy prettyprint lang-py tfo-signature-link">
<code>tf.compat.v1.estimator.tpu.TPUConfig(
    iterations_per_loop=2, num_shards=None, num_cores_per_replica=None,
    per_host_input_for_training=(True), tpu_job_name=None,
    initial_infeed_sleep_secs=None, input_partition_dims=None,
    eval_training_input_configuration=InputPipelineConfig.PER_HOST_V1,
    experimental_host_call_every_n_steps=1,
    experimental_allow_per_host_v2_parallel_get_next=(False),
    experimental_feed_hook=None
)
</code></pre>



<!-- Placeholder for "Used in" -->


<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Args</h2></th></tr>

<tr>
<td>
`iterations_per_loop`
</td>
<td>
This is the number of train steps running in TPU system
before returning to CPU host for each `Session.run`. This means global
step is increased `iterations_per_loop` times in one `Session.run`. It is
recommended to be set as number of global steps for next checkpoint. Note
that in evaluation don't use this value, instead we run total eval `steps`
on TPU for a single `Session.run`.
[Experimental]: `iterations_per_loop` can be specified as a time interval.
To specify N seconds in one `Session.run`, one can specify it as `Ns`
and substitute the N with the N with the number of desired seconds.
Alternatively, the unit of time can also be specified in minutes or
hours, e.g. `3600s` or `60m` or `1h`.
</td>
</tr><tr>
<td>
`num_shards`
</td>
<td>
(Deprecated, ignored by TPUEstimator). The number of model
replicas in the system. For non-model-parallelism case, this number equals
the total number of TPU cores. For model-parallelism, the total number of
TPU cores equals num_cores_per_replica * num_shards.
</td>
</tr><tr>
<td>
`num_cores_per_replica`
</td>
<td>
Defaults to `None`, which disables model parallelism.
An integer which describes the number of TPU cores per model replica. This
is required by model-parallelism which enables partitioning the model to
multiple cores. Currently num_cores_per_replica must be 1, 2, 4, or 8.
</td>
</tr><tr>
<td>
`per_host_input_for_training`
</td>
<td>
If `True`, for `PER_HOST_V1`, the `input_fn` is
invoked once on each host, and the number of hosts must be smaller or
equal to the number of replicas. For PER_HOST_V2, the `input_fn` is
invoked once for each host (if the number of hosts is less than the number
of replicas) or replica (if the number of replicas is less than the number
of hosts. With the per-core input pipeline configuration, it is invoked
once for each core. With a global batch size `train_batch_size` in
`TPUEstimator` constructor, the batch size for each shard is
`train_batch_size` // #hosts in the `True` or `PER_HOST_V1` mode. In
`PER_HOST_V2` mode, it is `train_batch_size` // #cores. In `BROADCAST`
mode, `input_fn` is only invoked once on host 0 and the tensors are
broadcasted to all other replicas. The batch size equals to
`train_batch_size`. With the per-core input pipeline configuration, the
shard batch size is also `train_batch_size` // #cores.
Note: per_host_input_for_training==PER_SHARD_V1 only supports mode.TRAIN.
</td>
</tr><tr>
<td>
`tpu_job_name`
</td>
<td>
The name of the TPU job. Typically, this name is auto-inferred
within TPUEstimator, however when using ClusterSpec propagation in more
esoteric cluster configurations, you may need to specify the job name as a
string.
</td>
</tr><tr>
<td>
`initial_infeed_sleep_secs`
</td>
<td>
The number of seconds the infeed thread should
wait before enqueueing the first batch. This helps avoid timeouts for
models that require a long compilation time.
</td>
</tr><tr>
<td>
`input_partition_dims`
</td>
<td>
A nested list to describe the partition dims for all
the tensors from input_fn(). The structure of input_partition_dims must
match the structure of `features` and `labels` from input_fn(). The total
number of partitions must match
`num_cores_per_replica`. For example, if input_fn() returns two tensors:
images with shape [N, H, W, C] and labels [N]. input_partition_dims =
[[1, 2, 2, 1], None] will split the images to 4 pieces and feed into 4
TPU cores. labels tensor are directly broadcasted to all the TPU cores
since the partition dims is `None`.
Current limitations: This feature is only supported with the PER_HOST_V2
input mode.
</td>
</tr><tr>
<td>
`eval_training_input_configuration`
</td>
<td>
If `SLICED`, `input_fn` is only invoked
once on host 0 and the tensors are broadcasted to all other replicas.
Unlike per_host_input_for_training=BROADCAST, each replica will only get a
slice of the data instead of a whole copy. If `PER_HOST_V1`, the behaviour
is determined by per_host_input_for_training.
</td>
</tr><tr>
<td>
`experimental_host_call_every_n_steps`
</td>
<td>
Within a training loop, this argument
sets how often host calls are performed during training. Host calls will
be evaluated every n steps within a training loop where n is the value of
this argument.
</td>
</tr><tr>
<td>
`experimental_allow_per_host_v2_parallel_get_next`
</td>
<td>
When enabled, allows
concurrent execution of dataset get next calls when using PER_HOST_V2
input. May result in a performance increase for models with a small step
time, but as a consequence TPUEstimator may non-deterministically
distribute batches to different cores, rather than guaranteeing round
robin behavior.
</td>
</tr><tr>
<td>
`experimental_feed_hook`
</td>
<td>
This is a class which user can provide to the TPU
estimator to override the default TPUInfeedOutfeedSessionHook implementation
and add customized implementatioin to handle infeed outfeed logic. If
given class is None, TPU estimator uses default TPUInfeedOutfeedSessionHook
implementation in tpu_estimator.py. If not None, TPU estimator uses this
customized tpu infeed outfeed session hook class rather to override the
default one.
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
If `num_cores_per_replica` is not 1, 2, 4, 8, ..., 128.
</td>
</tr>
</table>





<!-- Tabular view -->
 <table class="responsive fixed orange">
<colgroup><col width="214px"><col></colgroup>
<tr><th colspan="2"><h2 class="add-link">Attributes</h2></th></tr>

<tr>
<td>
`iterations_per_loop`
</td>
<td>

</td>
</tr><tr>
<td>
`num_shards`
</td>
<td>

</td>
</tr><tr>
<td>
`num_cores_per_replica`
</td>
<td>

</td>
</tr><tr>
<td>
`per_host_input_for_training`
</td>
<td>

</td>
</tr><tr>
<td>
`tpu_job_name`
</td>
<td>

</td>
</tr><tr>
<td>
`initial_infeed_sleep_secs`
</td>
<td>

</td>
</tr><tr>
<td>
`input_partition_dims`
</td>
<td>

</td>
</tr><tr>
<td>
`eval_training_input_configuration`
</td>
<td>

</td>
</tr><tr>
<td>
`experimental_host_call_every_n_steps`
</td>
<td>

</td>
</tr><tr>
<td>
`experimental_allow_per_host_v2_parallel_get_next`
</td>
<td>

</td>
</tr><tr>
<td>
`experimental_feed_hook`
</td>
<td>

</td>
</tr>
</table>



## Class Variables

* `eval_training_input_configuration` <a id="eval_training_input_configuration"></a>
* `experimental_allow_per_host_v2_parallel_get_next` <a id="experimental_allow_per_host_v2_parallel_get_next"></a>
* `experimental_feed_hook` <a id="experimental_feed_hook"></a>
* `experimental_host_call_every_n_steps` <a id="experimental_host_call_every_n_steps"></a>
* `initial_infeed_sleep_secs` <a id="initial_infeed_sleep_secs"></a>
* `input_partition_dims` <a id="input_partition_dims"></a>
* `iterations_per_loop` <a id="iterations_per_loop"></a>
* `num_cores_per_replica` <a id="num_cores_per_replica"></a>
* `num_shards` <a id="num_shards"></a>
* `per_host_input_for_training` <a id="per_host_input_for_training"></a>
* `tpu_job_name` <a id="tpu_job_name"></a>
