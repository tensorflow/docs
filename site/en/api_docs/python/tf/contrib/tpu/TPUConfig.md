page_type: reference
<style> table img { max-width: 100%; } </style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.TPUConfig

## Class `TPUConfig`





Defined in [`tensorflow/contrib/tpu/python/tpu/tpu_config.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.9/tensorflow/contrib/tpu/python/tpu/tpu_config.py).

TPU related configuration required by `TPUEstimator`.

#### Args:

* <b>`iterations_per_loop`</b>: This is the number of train steps running in TPU
    system before returning to CPU host for each `Session.run`. This means
    global step is increased `iterations_per_loop` times in one `Session.run`.
    It is recommended to be set as number of global steps for next checkpoint.
* <b>`num_shards`</b>: (Deprecated, ignored by TPUEstimator).
    The number of model replicas in the system. For non-model-parallelism
    case, this number equals the total number of TPU cores. For
    model-parallelism, the total number of TPU cores equals
    product(computation_shape) * num_shards.
* <b>`computation_shape`</b>: Defaults to `None`, which disables model parallelism. A
    list of size 3 which describes the shape of a model replica's block of
    cores. This is required by model-parallelism which enables partitioning
    the model to multiple cores. For example, [2, 2, 1] means the model is
    partitioned across 4 cores which span two cores in both x and y
    coordinates.  Please refer to <a href="../../../tf/contrib/tpu/Topology"><code>tf.contrib.tpu.Topology</code></a> for the
    geometry of a TPU mesh.
* <b>`per_host_input_for_training`</b>: If `True`, `PER_HOST_V1`, or `PER_HOST_V2`,
    `input_fn` is invoked per-host rather than per-core. With per-host input
    pipeline configuration, `input_fn` is invoked once on each host. With the
    per-core input pipeline configuration, it is invoked once for each core.
    With a global batch size `train_batch_size` in `TPUEstimator` constructor,
    the batch size for each shard is `train_batch_size` // #hosts in the
    `True` or `PER_HOST_V1` mode. In `PER_HOST_V2` mode, it is
    `train_batch_size` // #cores. With the per-core input pipeline
    configuration, the shard batch size is also `train_batch_size` // #cores.
* <b>`Note`</b>: per_host_input_for_training==PER_SHARD_V1 only supports mode.TRAIN.
* <b>`tpu_job_name`</b>: The name of the TPU job. Typically, this name is auto-inferred
    within TPUEstimator, however when using ClusterSpec propagation in more
    esoteric cluster configurations, you may need to specify the job name as a
    string.
* <b>`initial_infeed_sleep_secs`</b>: The number of seconds the infeed thread should
    wait before enqueueing the first batch. This helps avoid timeouts for
    models that require a long compilation time.

* <b>`Raises`</b>: * <b>`ValueError`</b>: If `computation_shape` or `computation_shape` are invalid.

## Properties

<h3 id="computation_shape"><code>computation_shape</code></h3>

Alias for field number 2

<h3 id="initial_infeed_sleep_secs"><code>initial_infeed_sleep_secs</code></h3>

Alias for field number 5

<h3 id="iterations_per_loop"><code>iterations_per_loop</code></h3>

Alias for field number 0

<h3 id="num_shards"><code>num_shards</code></h3>

Alias for field number 1

<h3 id="per_host_input_for_training"><code>per_host_input_for_training</code></h3>

Alias for field number 3

<h3 id="tpu_job_name"><code>tpu_job_name</code></h3>

Alias for field number 4



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
@staticmethod
__new__(
    cls,
    iterations_per_loop=2,
    num_shards=None,
    computation_shape=None,
    per_host_input_for_training=True,
    tpu_job_name=None,
    initial_infeed_sleep_secs=None
)
```





