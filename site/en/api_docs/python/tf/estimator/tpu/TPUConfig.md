page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.estimator.tpu.TPUConfig


<table class="tfo-notebook-buttons tfo-api" align="left">

<td>
  <a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/tpu_config.py">
    <img src="https://www.tensorflow.org/images/GitHub-Mark-32px.png" />
    View source on GitHub
  </a>
</td></table>



## Class `TPUConfig`

TPU related configuration required by `TPUEstimator`.



### Aliases:

* Class <a href="/api_docs/python/tf/estimator/tpu/TPUConfig"><code>tf.compat.v1.estimator.tpu.TPUConfig</code></a>
* Class <a href="/api_docs/python/tf/estimator/tpu/TPUConfig"><code>tf.contrib.tpu.TPUConfig</code></a>


<!-- Placeholder for "Used in" -->


#### Args:


* <b>`iterations_per_loop`</b>: This is the number of train steps running in TPU
  system before returning to CPU host for each <a href="../../../tf/InteractiveSession#run"><code>Session.run</code></a>. This means
  global step is increased `iterations_per_loop` times in one <a href="../../../tf/InteractiveSession#run"><code>Session.run</code></a>.
  It is recommended to be set as number of global steps for next checkpoint.
  Note that in evaluation don't use this value, instead we run total eval
  `steps` on TPU for a single <a href="../../../tf/InteractiveSession#run"><code>Session.run</code></a>.
  [Experimental]: `iterations_per_loop` can be specified as a time interval.
  To specify N seconds in one <a href="../../../tf/InteractiveSession#run"><code>Session.run</code></a>, one can specify it as `Ns` and
  substitute the N with the N with the number of desired seconds.
  Alternatively, the unit of time can also be specified in minutes or hours,
  e.g. `3600s` or `60m` or `1h`.
* <b>`num_shards`</b>: (Deprecated, ignored by TPUEstimator).
  The number of model replicas in the system. For non-model-parallelism
  case, this number equals the total number of TPU cores. For
  model-parallelism, the total number of TPU cores equals
  num_cores_per_replica * num_shards.
* <b>`num_cores_per_replica`</b>: Defaults to `None`, which disables model parallelism.
  An integer which describes the number of TPU cores per model replica. This
  is required by model-parallelism which enables partitioning
  the model to multiple cores. Currently num_cores_per_replica must be
  1, 2, 4, or 8.
* <b>`per_host_input_for_training`</b>: If `True`, for `PER_HOST_V1`, the `input_fn` is
  invoked once on each host, and the number of hosts must be smaller or
  equal to the number of replicas. For PER_HOST_V2, the `input_fn` is
  invoked once for each host (if the number of hosts is less than the number
  of replicas) or replica (if the number of replicas is less than the number
  of hosts. With the per-core input pipeline configuration, it is invoked
  once for each core.
  With a global batch size `train_batch_size` in `TPUEstimator` constructor,
  the batch size for each shard is `train_batch_size` // #hosts in the
  `True` or `PER_HOST_V1` mode. In `PER_HOST_V2` mode, it is
  `train_batch_size` // #cores. In `BROADCAST` mode, `input_fn` is only
  invoked once on host 0 and the tensors are broadcasted to all other
  replicas. The batch size equals to `train_batch_size`. With the per-core
  input pipeline configuration, the shard batch size is also
  `train_batch_size` // #cores.
  Note: per_host_input_for_training==PER_SHARD_V1 only supports mode.TRAIN.
* <b>`tpu_job_name`</b>: The name of the TPU job. Typically, this name is auto-inferred
  within TPUEstimator, however when using ClusterSpec propagation in more
  esoteric cluster configurations, you may need to specify the job name as a
  string.
* <b>`initial_infeed_sleep_secs`</b>: The number of seconds the infeed thread should
  wait before enqueueing the first batch. This helps avoid timeouts for
  models that require a long compilation time.
* <b>`input_partition_dims`</b>: A nested list to describe the partition dims
  for all the tensors from input_fn(). The structure of
  input_partition_dims must match the structure of `features` and
  `labels` from input_fn(). The total number of partitions must match
  `num_cores_per_replica`. For example, if input_fn() returns two tensors:
  images with shape [N, H, W, C] and labels [N].
  input_partition_dims = [[1, 2, 2, 1], None] will split the images to 4
  pieces and feed into 4 TPU cores. labels tensor are directly broadcasted
  to all the TPU cores since the partition dims is `None`.
  Current limitations: This feature is only supported with the PER_HOST_V2
  input mode.
* <b>`eval_training_input_configuration`</b>: If `SLICED`, `input_fn` is only
  invoked once on host 0 and the tensors are broadcasted to all other
  replicas. Unlike per_host_input_for_training=BROADCAST, each replica will
  only get a slice of the data instead of a whole copy. If `PER_HOST_V1`,
  the behaviour is determined by per_host_input_for_training.
* <b>`experimental_host_call_every_n_steps`</b>: Within a training loop, this argument
  sets how often host calls are performed during training. Host calls will
  be evaluated every n steps within a training loop where n is the value of
  this argument.


#### Raises:


* <b>`ValueError`</b>: If `num_cores_per_replica` is not 1, 2, 4, 8, ..., 128.

<h2 id="__new__"><code>__new__</code></h2>

<a target="_blank" href="https://github.com/tensorflow/estimator/tree/master/tensorflow_estimator/python/estimator/tpu/tpu_config.py">View source</a>

``` python
@staticmethod
__new__(
    cls,
    iterations_per_loop=2,
    num_shards=None,
    num_cores_per_replica=None,
    per_host_input_for_training=True,
    tpu_job_name=None,
    initial_infeed_sleep_secs=None,
    input_partition_dims=None,
    eval_training_input_configuration=InputPipelineConfig.PER_HOST_V1,
    experimental_host_call_every_n_steps=1
)
```

Create new instance of TPUConfig(iterations_per_loop, num_shards, num_cores_per_replica, per_host_input_for_training, tpu_job_name, initial_infeed_sleep_secs, input_partition_dims, eval_training_input_configuration, experimental_host_call_every_n_steps)




## Properties

<h3 id="iterations_per_loop"><code>iterations_per_loop</code></h3>




<h3 id="num_shards"><code>num_shards</code></h3>




<h3 id="num_cores_per_replica"><code>num_cores_per_replica</code></h3>




<h3 id="per_host_input_for_training"><code>per_host_input_for_training</code></h3>




<h3 id="tpu_job_name"><code>tpu_job_name</code></h3>




<h3 id="initial_infeed_sleep_secs"><code>initial_infeed_sleep_secs</code></h3>




<h3 id="input_partition_dims"><code>input_partition_dims</code></h3>




<h3 id="eval_training_input_configuration"><code>eval_training_input_configuration</code></h3>




<h3 id="experimental_host_call_every_n_steps"><code>experimental_host_call_every_n_steps</code></h3>
