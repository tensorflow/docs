page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.contrib.tpu.TPUConfig

## Class `TPUConfig`





Defined in [`tensorflow/contrib/tpu/python/tpu/tpu_config.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.10/tensorflow/contrib/tpu/python/tpu/tpu_config.py).

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
* <b>`num_cores_per_replica`</b>: Defaults to `None`, which disables model parallelism.
    An integer which describes the number of TPU cores per model replica. This
    is required by model-parallelism which enables partitioning
    the model to multiple cores. Currently num_cores_per_replica must be
    1, 2, 4, or 8.
* <b>`per_host_input_for_training`</b>: If `True`, `PER_HOST_V1`, or `PER_HOST_V2`,
    `input_fn` is invoked once on each host. With the per-core input pipeline
    configuration, it is invoked once for each core.
    With a global batch size `train_batch_size` in `TPUEstimator` constructor,
    the batch size for each shard is `train_batch_size` // #hosts in the
    `True` or `PER_HOST_V1` mode. In `PER_HOST_V2` mode, it is
    `train_batch_size` // #cores. In `BROADCAST` mode, `input_fn` is only
    invoked once on host 0 and the tensors are broadcasted to all other
    replicas. The batch size equals to train_batch_size`. With the per-core
    input pipeline configuration, the shard batch size is also
    `train_batch_size` // #cores.
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

<h3 id="initial_infeed_sleep_secs"><code>initial_infeed_sleep_secs</code></h3>

Alias for field number 5

<h3 id="iterations_per_loop"><code>iterations_per_loop</code></h3>

Alias for field number 0

<h3 id="num_cores_per_replica"><code>num_cores_per_replica</code></h3>

Alias for field number 2

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
    num_cores_per_replica=None,
    per_host_input_for_training=True,
    tpu_job_name=None,
    initial_infeed_sleep_secs=None
)
```





