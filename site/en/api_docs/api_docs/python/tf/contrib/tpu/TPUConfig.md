

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->


# tf.contrib.tpu.TPUConfig

## Class `TPUConfig`





Defined in [`tensorflow/contrib/tpu/python/tpu/tpu_config.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.4/tensorflow/contrib/tpu/python/tpu/tpu_config.py).

TPU related configuration required by `TPUEstimator`.

#### Args:

* <b>`iterations_per_loop`</b>: This is the number of train steps runnining in TPU
    system before returning to CPU host for each `Session.run`. This means
    global step is increased `iterations_per_loop` times in one `Session.run`.
    It is recommended to be set as number of global steps for next checkpoint.
* <b>`num_shards`</b>: The number of TPU shards in the system.
* <b>`per_host_input_for_training`</b>: If `True`, `input_fn` is invoked per host
    rather than per shard. Note: This behavior is going to be default as
    `True` soon, so this flag will be removed after that. Also note that this
    only works for single-host TPU training now.

## Properties

<h3 id="iterations_per_loop"><code>iterations_per_loop</code></h3>

Alias for field number 0

<h3 id="num_shards"><code>num_shards</code></h3>

Alias for field number 1

<h3 id="per_host_input_for_training"><code>per_host_input_for_training</code></h3>

Alias for field number 2



## Methods

<h3 id="__new__"><code>__new__</code></h3>

``` python
@staticmethod
__new__(
    cls,
    iterations_per_loop=2,
    num_shards=2,
    per_host_input_for_training=False
)
```





