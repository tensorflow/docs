page_type: reference
<style>{% include "site-assets/css/style.css" %}</style>

<!-- DO NOT EDIT! Automatically generated file. -->

# tf.keras.initializers.VarianceScaling

## Class `VarianceScaling`

Inherits From: [`Initializer`](../../../tf/keras/initializers/Initializer)

### Aliases:

* Class `tf.initializers.variance_scaling`
* Class `tf.keras.initializers.VarianceScaling`
* Class `tf.variance_scaling_initializer`



Defined in [`tensorflow/python/ops/init_ops.py`](https://github.com/tensorflow/tensorflow/blob/r1.13/tensorflow/python/ops/init_ops.py).

Initializer capable of adapting its scale to the shape of weights tensors.

With `distribution="truncated_normal" or "untruncated_normal"`,
samples are drawn from a truncated/untruncated normal
distribution with a mean of zero and a standard deviation (after truncation,
if used) `stddev = sqrt(scale / n)`
where n is:
  - number of input units in the weight tensor, if mode = "fan_in"
  - number of output units, if mode = "fan_out"
  - average of the numbers of input and output units, if mode = "fan_avg"

With `distribution="uniform"`, samples are drawn from a uniform distribution
within [-limit, limit], with `limit = sqrt(3 * scale / n)`.

#### Args:

* <b>`scale`</b>: Scaling factor (positive float).
* <b>`mode`</b>: One of "fan_in", "fan_out", "fan_avg".
* <b>`distribution`</b>: Random distribution to use. One of "normal", "uniform".
* <b>`seed`</b>: A Python integer. Used to create random seeds. See
    <a href="../../../tf/random/set_random_seed"><code>tf.set_random_seed</code></a>
    for behavior.
* <b>`dtype`</b>: Default data type, used if no `dtype` argument is provided when
    calling the initializer. Only floating point types are supported.


#### Raises:

* <b>`ValueError`</b>: In case of an invalid value for the "scale", mode" or
    "distribution" arguments.

<h2 id="__init__"><code>__init__</code></h2>

``` python
__init__(
    scale=1.0,
    mode='fan_in',
    distribution='truncated_normal',
    seed=None,
    dtype=tf.dtypes.float32
)
```

DEPRECATED FUNCTION ARGUMENT VALUES

Warning: SOME ARGUMENT VALUES ARE DEPRECATED: `(distribution='normal')`. They will be removed in a future version.
Instructions for updating:
`normal` is a deprecated alias for `truncated_normal`



## Methods

<h3 id="__call__"><code>__call__</code></h3>

``` python
__call__(
    shape,
    dtype=None,
    partition_info=None
)
```

Returns a tensor object initialized as specified by the initializer.

#### Args:

* <b>`shape`</b>: Shape of the tensor.
* <b>`dtype`</b>: Optional dtype of the tensor. If not provided use the initializer
    dtype.
* <b>`partition_info`</b>: Optional information about the possible partitioning of a
    tensor.

<h3 id="from_config"><code>from_config</code></h3>

``` python
from_config(
    cls,
    config
)
```

Instantiates an initializer from a configuration dictionary.

Example:

```python
initializer = RandomUniform(-1, 1)
config = initializer.get_config()
initializer = RandomUniform.from_config(config)
```

#### Args:

* <b>`config`</b>: A Python dictionary.
    It will typically be the output of `get_config`.


#### Returns:

An Initializer instance.

<h3 id="get_config"><code>get_config</code></h3>

``` python
get_config()
```

Returns the configuration of the initializer as a JSON-serializable dict.

#### Returns:

A JSON-serializable Python dict.



