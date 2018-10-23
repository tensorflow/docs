

page_type: reference


<!-- DO NOT EDIT! Automatically generated file. -->
# tf.random_normal_initializer

### `class tf.random_normal_initializer`



Defined in [`tensorflow/python/ops/init_ops.py`](https://www.github.com/tensorflow/tensorflow/blob/r1.1/tensorflow/python/ops/init_ops.py).

See the guide: [Variables > Sharing Variables](../../../api_guides/python/state_ops#Sharing_Variables)

Initializer that generates tensors with a normal distribution.

#### Args:

* <b>`mean`</b>: a python scalar or a scalar tensor. Mean of the random values
    to generate.
* <b>`stddev`</b>: a python scalar or a scalar tensor. Standard deviation of the
    random values to generate.
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
    [`tf.set_random_seed`](../tf/set_random_seed)
    for behavior.
* <b>`dtype`</b>: The data type. Only floating point types are supported.

## Methods

<h3 id="__init__"><code>__init__</code></h3>

``` python
__init__(
    mean=0.0,
    stddev=1.0,
    seed=None,
    dtype=tf.float32
)
```



<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    shape,
    dtype=None,
    partition_info=None
)
```





